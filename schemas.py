from typing import Optional
from pydantic import BaseModel

class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    company_name: str
    city: str
    state: str
    zip: int
    email: str
    web: str
    age: int


class UserUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    company_name: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    zip: Optional[int] = None
    email: Optional[str] = None
    web: Optional[str] = None
    age: Optional[int] = None
