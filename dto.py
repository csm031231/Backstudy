from pydantic import BaseModel
from typing import Optional

class UpdateUserDTO(BaseModel):
    username : Optional[str] = None   # 풀 네임 (선택적)
    password: Optional[str] = None    # 비밀번호 (선택적)


class AddUserDTO(BaseModel):
    username: str
    password: str
    email: Optional[str] = None 

class DeleteUserDTO(BaseModel):
    username: str  

class GetUserDTO(BaseModel):
    username: str

class LoginDTO(BaseModel):
    username: str
    password: str