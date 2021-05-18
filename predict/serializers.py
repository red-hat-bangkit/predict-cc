from pydantic import BaseModel
from typing import Optional


class BencanaType(BaseModel):
    name: str
    capital: Optional[str] = None