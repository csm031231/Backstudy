# User 모델 정의
from sqlalchemy import Column, Integer, String, DateTime, func
from base import Base
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, autoincrement=True)  # 자동 증가 ID
    username = Column(String(50), unique=True, nullable=False)  # 유저 이름 (고유, 필수)
    password = Column(String(255), nullable=False)             # 비밀번호 (필수)
    email = Column(String(100), unique=True)                   # 이메일 (고유, 선택)
    created_at = Column(DateTime, default=func.now())          # 계정 생성 시간 (자동)