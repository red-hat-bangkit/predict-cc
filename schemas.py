import graphene
from predict import schemas

class Query(
    schemas.Query, 
    graphene.ObjectType):
    pass

class Mutations(
    schemas.PredictMutations,
    graphene.ObjectType):
    pass