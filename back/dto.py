from pydantic import BaseModel
from typing import Optional

class AddUserDTO(BaseModel):
    username: str
    email: str
    password: str

class UpdateUserDTO(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UserResponseDTO(BaseModel):
    username: str
    email: str

class LoginDTO(BaseModel):
    username: str
    password: str