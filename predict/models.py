from pydantic import BaseModel

class APIExceptionData(BaseModel):
    type: str
    msg: str

class APIException(BaseModel):
    detail: APIExceptionData

error_responses = {
    400: {"model": APIException, "description": "Bad Request"},
    401: {"model": APIException, "description": "Authorization Failed"}
}