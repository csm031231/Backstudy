from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session
from base import get_db
from model import User
from dto import UpdateUserDTO, AddUserDTO, DeleteUserDTO, GetUserDTO,LoginDTO
from security import hash_password, verify_password

router = APIRouter(
    prefix="/user",
)


@router.post("/")
def add_user(user_data: AddUserDTO, db: Session = Depends(get_db)):
    try:
        hashed_password = hash_password(user_data.password)  # 비밀번호 해싱
        new_user = User(
            username=user_data.username,
            password=hashed_password,
            email=user_data.email
        )
        db.add(new_user)
        db.commit()
        return {"message": f"User {user_data.username} added successfully!"}
    except Exception as e:
        db.rollback()
        return {"error": f"Error adding user: {str(e)}"}


@router.delete("/{username}/del")
def delete_user(username: str, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.username == username).first()
        if not user:
            return {"error": f"User {username} not found"}
        db.delete(user)
        db.commit()
        return {"message": f"User {username} deleted successfully!"}
    except Exception as e:
        db.rollback()
        return {"error": f"Error deleting user: {str(e)}"}


@router.put("/{username}/change")
def update_user(username: str, user_data:UpdateUserDTO, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.username == username).first()
        user.username = user_data.username
        user.password = user_data.password
        if user_data.password:
            user.password = hash_password(user_data.password)
        
        db.add(user)
        db.commit()
    except Exception as e:
        db.rollback()
        print("Error adding user:", e)

@router.get("/{username}/profile")
def get_user(user_data: GetUserDTO, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.username == user_data.username).first()
        if not user:
            return {"error": f"User {user_data.username} not found"}
        return {
            "username": user.username,
            "email": user.email
        }
    except Exception as e:
        return {"error": str(e)}

@router.post("/Login")
def login_user(user_data: LoginDTO, db: Session = Depends(get_db)):
    try:
        user = db.query(User).filter(User.username == user_data.username).first()
        if not user:
            return {"error": f"User {user_data.username} not found"}
        else:
            result=verify_password(user_data.password,user.password)
            if result:
                return {"welcome": f"User {user_data.username}"}
            else:
                return {"error": f"Wrong password"}
    except Exception as e:
        return {"error": str(e)}

