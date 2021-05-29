from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

# Graphql to Rest Translation Model
class City(BaseModel):
    name: str


class Location(BaseModel):
    name: str
    city: Optional[City] = None
    lat_long: Optional[str] = None

class Prediction(BaseModel):
    bencana: str
    location: Location
    confidence: Optional[float] = None
    rmse: Optional[float] = None
    time: Optional[datetime] = None
    is_bencana: Optional[bool] = None
    reason: str

class BencanaInCity(BaseModel):
    name: str
    city: City
    predictions: List[Prediction]

class BencanaInLocation(BaseModel):
    name: str
    location: Location
    prediction: Prediction

# Exception Model
class APIExceptionData(BaseModel):
    type: str
    msg: str

class APIException(BaseModel):
    detail: APIExceptionData

error_responses = {
    400: {"model": APIException, "description": "Bad Request"},
    401: {"model": APIException, "description": "Authorization Failed"}
}