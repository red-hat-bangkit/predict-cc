import graphene

from .serializers import BencanaType
from datetime import datetime

class Capital(graphene.ObjectType):
    name = graphene.String()

class Location(graphene.ObjectType):
    name = graphene.String()
    capital = graphene.Field(Capital)
    lat_long = graphene.String()

    def resolve_lat_long(self, info):
        lat_long_db = {"Ciliwung":"12345, 53421"}
        return lat_long_db.get(self.name)

class Prediction(graphene.ObjectType):
    bencana = graphene.String()
    location = graphene.Field(Location)
    confidence = graphene.Float()
    time = graphene.DateTime()
    reason = graphene.String()

class BencanaInCapital(graphene.ObjectType):
    name = graphene.String()
    capital = graphene.Field(Capital)
    predictions = graphene.List(Prediction)

    def resolve_predictions(self, info):
        ml_output = [
            (0.85, "Ciliwung", datetime.now(), "Curah Hujan"), 
            (0.75, "Ciamis", datetime.now(), "Luapan Sungai")]
        predictions = []
        for confidence, location_name, time_stamp, reason in ml_output:
            print(confidence)
            location = Location(name=location_name, capital=self.capital)
            predictions.append(
                Prediction(
                    bencana=self.name, 
                    confidence = confidence,
                    location=location, 
                    time=time_stamp,
                    reason=reason)
            )
        return predictions

class BencanaInLocation(graphene.ObjectType):
    name = graphene.String()
    location = graphene.Field(Location)
    prediction = graphene.Field(Prediction)

    def resolve_prediction(self, info):
        ml_output = (0.85, "Ciliwung", datetime.now(), "Curah Hujan")
        prediction = Prediction(
                        bencana=self.name, 
                        confidence = ml_output[0],
                        location=self.location, 
                        time=ml_output[2],
                        reason=ml_output[3])
        return prediction

class Query(graphene.AbstractType):
    hello_world = graphene.String()
    def resolve_hello_world(self, info):
        return "Hello World from FastAPI"

    bencana_in_capital = graphene.Field(BencanaInCapital,
                capital=graphene.String(required=True),
                name=graphene.String(required=True))
    def resolve_bencana_in_capital(self, info, name, capital):
        return BencanaInCapital(name=name, capital=Capital(name=capital))
    
    bencana_in_location = graphene.Field(BencanaInLocation,
                location_name=graphene.String(required=True),
                name=graphene.String(required=True))
    def resolve_bencana_in_location(self, info, name, location_name ):
        return BencanaInLocation(name=name, location=Location(name=location_name))


class GetBencana(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        capital = graphene.String()
    
    bencana = graphene.String()
    @staticmethod
    def mutate(root, info, name, capital):
        return GetBencana(bencana=f"{name}, {capital}") 


class PredictMutations(graphene.AbstractType):
    get_bencana = GetBencana.Field()
