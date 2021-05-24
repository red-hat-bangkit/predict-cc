import requests
from fastapi import Request, Depends
from settings.settings import os

from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

http_bearer = HTTPBearer()

def firebase_auth(request: Request, auth: HTTPAuthorizationCredentials = Depends(http_bearer)):
        payload = {
            "idToken": auth.credentials
        }
        resp = requests.post(
            "https://identitytoolkit.googleapis.com/v1/accounts:lookup?key=%s"%os.environ.get("FIREBASE_WEB_API_KEY", ""),
            data=payload
        )
        if resp.status_code == 200:
            return resp.json()
        else:
            return None