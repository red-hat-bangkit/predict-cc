from starlette.middleware.base import BaseHTTPMiddleware

from .database import SessionLocal
class DBSessionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request, call_next):
        try:
            request.state.db = SessionLocal
            response = await call_next(request)
        finally:
            request.state.db.remove()
        return response

