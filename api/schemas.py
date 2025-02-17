from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime

class UserSchema(BaseModel):
  id: int
  name: str
  email: EmailStr
  
  class Config:
    from_attributes = True


class CreateUserSchema(BaseModel):
  id: int
  name: str
  email: EmailStr
  password: str
  
  class Config:
    from_attributes = True


class LoginSchema(BaseModel):
  email: EmailStr
  password: str


class Token(BaseModel):
  access_token: str
  token_type: str


class TokenData(BaseModel):
  id: Optional[int] = None