import graphene

from datetime import datetime

class City(graphene.ObjectType):
    name = graphene.String()

class Location(graphene.ObjectType):
    name = graphene.String()
    city = graphene.Field(City)
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

class BencanaInCity(graphene.ObjectType):
    name = graphene.String()
    city = graphene.Field(City)
    predictions = graphene.List(Prediction)

    def resolve_predictions(self, info):
        ml_output = [
            (0.85, "Ciliwung", datetime.now(), "Curah Hujan"), 
            (0.75, "Ciamis", datetime.now(), "Luapan Sungai")]
        predictions = []
        for confidence, location_name, time_stamp, reason in ml_output:
            location = Location(name=location_name, city=self.city)
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

    bencana_in_city = graphene.Field(BencanaInCity,
                city=graphene.String(required=True),
                name=graphene.String(required=True))
    def resolve_bencana_in_city(self, info, name, city):
        return BencanaInCity(name=name, city=City(name=city))
    
    bencana_in_location = graphene.Field(BencanaInLocation,
                location_name=graphene.String(required=True),
                name=graphene.String(required=True))
    def resolve_bencana_in_location(self, info, name, location_name ):
        return BencanaInLocation(name=name, location=Location(name=location_name))


class GetBencana(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        city = graphene.String()
    
    bencana = graphene.String()
    @staticmethod
    def mutate(root, info, name, city):
        return GetBencana(bencana=f"{name}, {city}") 


class PredictMutations(graphene.AbstractType):
    get_bencana = GetBencana.Field()
