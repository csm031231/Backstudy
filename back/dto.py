from pydantic import BaseModel
from typing import Optional

class UserCreateDTO(BaseModel):
    username: str
    email: str
    password: str

class UserUpdateDTO(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserResponseDTO(BaseModel):
    username: str
    email: str

class UserLoginDTO(BaseModel):
    username: str
    password: str