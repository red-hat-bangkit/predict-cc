from fastapi import APIRouter, Query
from typing import List, Optional
from datetime import datetime
from ml.models_loader import predict_banjir, get_supported_locations
import pandas as pd

from predict.models import (
    Location,
    Prediction,
    BencanaInCity,
    BencanaInLocation,
    City,
)

router = APIRouter()
def get_lat_long(location: str):
    loc_to_latlong = {
        "Gambir": "2.214740,102.655861",
        "Kelapa Gading": "-6.158950,106.916641" 
    }
    return loc_to_latlong.get(location, None)


@router.get("/predictions", 
    response_model=List[Prediction], 
    description="Get predictions of specific bencana. Always return predictions.")
async def list_predictions(
    bencana_name: str = Query(..., description="Bencana type", example="banjir"), 
    location_name: str = Query(..., description="Location name", example="Kampung Kelapa"),
    future_days: Optional[int] = Query(10, description="How many days ahead to predict. Default 10"), 
    after_date: Optional[str] = Query(None, description="predict after specific date in [yyy-mm-dd], example: 2019-12-14")):
    
    if after_date:
        output, col_name = predict_banjir(location_name, future_days=future_days, after_date=after_date)
    else:
        output, col_name = predict_banjir(location_name, future_days=future_days)
    # ('prediction', 'rmse', 'forecasted_rainfall', 'date')
    ml_outputs = pd.DataFrame(output, columns = col_name)

    predictions = []
    for idx, output in ml_outputs.iterrows():
        location = Location(name=location_name, lat_long=get_lat_long(location_name))
        prediction = Prediction(
                        bencana=bencana_name, 
                        confidence = None, # not supported yet -> fallback to rmse
                        rmse = output["rmse"],
                        location= location, 
                        time= output["date"],
                        is_bencana = output["prediction"],
                        reason= "Curah hujan (%s mm)"%output["forecasted_rainfall"])
        predictions.append(prediction)

    return predictions

@router.get("/predictions:bencanaInLocation", 
    response_model=List[Prediction],
    description="Get predictions of specific bencana. Return empty list if no bencana predicted.")
async def get_banjir_predictions(
    bencana_name: str = Query(..., description="Bencana type", example="banjir"), 
    location_name: str = Query(..., description="Location name", example="Kampung Kelapa"),
    future_days: Optional[int] = Query(10, description="How many days ahead to predict. Default 10"), 
    after_date: Optional[str] = Query(None, description="predict after specific date in [yyy-mm-dd]", example="2019-12-14")):

    if after_date:
        output, col_name = predict_banjir(location_name, future_days=future_days, after_date=after_date)
    else:
        output, col_name = predict_banjir(location_name, future_days=future_days)
    # ('prediction', 'rmse', 'forecasted_rainfall', 'date')
    ml_outputs = pd.DataFrame(output, columns = col_name)
    ml_outputs = ml_outputs[ml_outputs["prediction"] == 1.0]

    predictions = []
    for idx, output in ml_outputs.iterrows():
        location = Location(name=location_name, lat_long=get_lat_long(location_name))
        prediction = Prediction(
                        bencana=bencana_name, 
                        confidence = None, # not supported yet -> fallback to rmse
                        rmse = output["rmse"],
                        location= location, 
                        time= output["date"],
                        is_bencana = output["prediction"],
                        reason= "Curah hujan (%s mm)"%output["forecasted_rainfall"])
        predictions.append(prediction)

    return predictions


@router.get("/predictions/locations", 
    response_model=List[Location], 
    description="Supported predictions locations")
async def predictions_locations():
    locations = []
    for location in get_supported_locations():
        locations.append(Location(name=location, lat_long=get_lat_long(location)))
    return locations

@router.get("/predictions:bencanaInCity", response_model=List[Prediction], deprecated=True)
async def prediction_in_city(bencana_name: str, city_name: str):
    ml_output = [
        (0.85, "Gambir", datetime.now(), "Curah Hujan"), 
        (0.75, "Kelapa Gading", datetime.now(), "Luapan Sungai")]
    predictions = []

    city = City(name=city_name)
    for confidence, location_name, time_stamp, reason in ml_output:
        location = Location(name=location_name, city=city, lat_long=get_lat_long(location_name))
        predictions.append(
            Prediction(
                bencana=bencana_name, 
                confidence = confidence,
                location=location, 
                time=time_stamp,
                reason=reason)
        )

    return predictions
