import requests
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
from firebase_admin.exceptions import FirebaseError

from settings.settings import os
from .exceptions import APIException, api_exception_handler, ErrorTypes, HTTP_OF_GRPC


class FirebaseAuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        payload = {
            "idToken": request.headers.get("Authorization", "Bearer JWT_TOKEN").split(" ")[1],
        }
        resp = requests.post(
            "https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=%s"%os.environ.get("FIREBASE_WEB_API_KEY", ""),
            data=payload
        )
        if resp.status_code == 200:
            request.state.user = resp.json()
            response = await call_next(request)
        else:
            request.state.user = None
            response = await call_next(request)
        return response

class GlobalExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            response = await call_next(request)
        except ValueError as err:
            return await api_exception_handler(
                request,
                APIException(400, ErrorTypes.VALUE_ERROR, str(err))
            )
        except FirebaseError as err:
            return await api_exception_handler(
                request,
                APIException(HTTP_OF_GRPC[err.code], ErrorTypes.FIREBASE_ERROR, str(err))
            )
        except Exception as err:
            return await api_exception_handler(
                request, 
                APIException(500, ErrorTypes.GENERAL_EXCEPTION, str(err))
            )
        return response


def init_middlewares(app: FastAPI):
    app.add_middleware(GlobalExceptionMiddleware)