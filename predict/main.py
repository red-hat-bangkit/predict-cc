from fastapi import FastAPI
from .rest.v1.auth.api import router as auth_router
from .rest.v1.prediction.api import router as prediction_router
from .exceptions import init_exceptions
from .middlewares import init_middlewares
from .gql.main import gql_app

app = FastAPI(
    title="PREDICT (PRE DIsaster Consciousness Tips",
    description="Predict disasters so citizen can prepare",
    version="0.0.1",
)

init_exceptions(app)

init_middlewares(app)

app.add_route("/gql", gql_app)
app.include_router(prediction_router, prefix="/v1")