from fastapi.responses import JSONResponse
from fastapi import Request

# APIException
from enum import Enum
from fastapi import FastAPI
from .models import APIException as APIExceptionModel, APIExceptionData as APIExceptionDataModel

class ErrorTypes(str, Enum):
    VALIDATION_ERROR = "Validation Error"
    VALUE_ERROR = "Value Error"
    GENERAL_EXCEPTION = "General Exception"
    FIREBASE_ERROR = "Firebase Error"
    UNAUTHENTICATED = "Unauthenticated"
    UNAUTHORIZED = "Unauthorized"

HTTP_OF_GRPC =  {
    "OK":200,
    "INVALID_ARGUMENT": 400,
    "FAILED_PRECONDITION": 400,
    "OUT_OF_RANGE": 400,
    "UNAUTHENTICATED": 401,
    "PERMISSION_DENIED": 403,
    "NOT_FOUND": 404,
    "ABORTED": 409,
    "ALREADY_EXISTS": 409,
    "RESOURCE_EXHAUSTED": 429,
    "CANCELLED": 499,
    "DATA_LOSS": 500,
    "UNKNOWN": 500,
    "INTERNAL": 500,
    "NOT_IMPLEMENTED": 501,
    "N/A": 502,
    "UNAVAILABLE": 503,
    "DEADLINE_EXCEEDED": 504
}

class APIException(Exception):
    def __init__(self, status_code: int, error: ErrorTypes, message: str):
        self.status_code = status_code
        self.error = error
        self.message = message

async def api_exception_handler(request: Request, exc: APIException):
    return JSONResponse(
        status_code=exc.status_code,
        content=APIExceptionModel(
                    detail=APIExceptionDataModel(
                        type=exc.error, 
                        msg=exc.message
                    )
                ).dict()
    )

def init_exceptions(app: FastAPI):
    app.add_exception_handler(APIException, api_exception_handler)