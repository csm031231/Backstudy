from fastapi import APIRouter,Depends,HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from base import get_db
from model import User
from dto import UpdateUserDTO, AddUserDTO
from security import hash_password, verify_password, oauth2_scheme,create_access_token,authenticate_user,get_current_user

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
def delete_user(db: Session = Depends(get_db),user:str=Depends(get_current_user)):
    try:
        user = db.query(User).filter(User.username == user).first()
        if not user:
            return {"error": f"User {user} not found"}
        db.delete(user)
        db.commit()
        return {"message": f"User {user} deleted successfully!"}
    except Exception as e:
        db.rollback()
        return {"error": f"Error deleting user: {str(e)}"}

@router.put("/{username}/change")
def update_user(user_data:UpdateUserDTO, db: Session = Depends(get_db),user:str=Depends(get_current_user)):
    try:
        user = db.query(User).filter(User.username == user).first()
        user.username = user_data.username
        user.password = user_data.password
        if user_data.password:
            user.password = hash_password(user_data.password)
        
        db.add(user)
        db.commit()
        return {"message": f"User {user} update successfully!"}
    except Exception as e:
        db.rollback()
        print("Error adding user:", e)

@router.get("/{username}/profile")
def get_user(db: Session = Depends(get_db),user:str=Depends(get_current_user)):
    try:
        user = db.query(User).filter(User.username == user).first()
        if not user:
            return {"error": f"User {user} not found"}
        return {
            "username": user.username,
            "email": user.email
        }
    except Exception as e:
        return {"error": str(e)}

@router.post("/Login")
async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
    """
    🔑 로그인 처리 및 토큰 발급
    """
    # 사용자 인증
    if authenticate_user(form_data.username, form_data.password):
        # 토큰 데이터 준비
        token_data = {
            "sub": form_data.username,
            "type": "access"
        }

        # 토큰 생성 및 반환
        token = create_access_token(token_data)
        return {"access_token": token, "token_type": "bearer"}
    else:
        raise HTTPException(
            status_code=401,
            detail="아이디 또는 비밀번호가 잘못되었습니다"
        )

