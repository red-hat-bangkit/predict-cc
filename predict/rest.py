from fastapi import APIRouter, HTTPException, Request, Header, Depends
from typing import Optional
from fastapi.responses import JSONResponse

import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin.exceptions import FirebaseError

from settings.settings import os

from .exceptions import APIException, ErrorTypes, HTTP_OF_GRPC
from .models import error_responses

cred = credentials.Certificate(os.environ.get("GOOGLE_APPLICATION_CREDENTIALS", ""))
firebase_app = firebase_admin.initialize_app(cred)
auth.Client(firebase_app)

router = APIRouter()

@router.get("/appname")
def app_name():
    return firebase_app.project_id

@router.get("/users")
def list_users():
    return auth.list_users()

@router.post("/users", responses={**error_responses})
def create_user(email: str, password: str):
    user = auth.create_user(email=email, password=password)
    return user

from .authentication import firebase_auth
@router.get("/users:get", responses={**error_responses})
def get_user(request: Request, user = Depends(firebase_auth)):
    # user = auth.get_user_by_email(email=email)
    if user:
        return user
    else:
        raise APIException(401, ErrorTypes.UNAUTHORIZED, "Authorization Failed.")

import requests
@router.post("/users:signInWithPassword", responses={**error_responses})
def login_user(email: str, password: str):
    payload = {
        "email": email,
        "password": password,
        "returnSecureToken": True
    }
    response = requests.post(
        "https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key=%s"%os.environ.get("FIREBASE_WEB_API_KEY"),
        data = payload
    )
    return response.json()