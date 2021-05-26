from fastapi import APIRouter
from typing import List
from datetime import datetime

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

@router.get("/predictions:bencanaInCity", response_model=List[Prediction])
async def list_predictions(bencana_name: str, city_name: str):

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


@router.get("/predictions:bencanaInLocation", response_model=Prediction)
async def get_prediction(bencana_name: str, location_name: str):
    ml_output = (0.85, "Gambir", "-6.158950,106.916641", datetime.now(), "Curah Hujan")

    location = Location(name=location_name, lat_long=ml_output[2])
    prediction = Prediction(
                    bencana=bencana_name, 
                    confidence = ml_output[0],
                    location=location, 
                    time=ml_output[3],
                    reason=ml_output[4])
    return prediction