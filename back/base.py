# PostgreSQL 데이터베이스 연결을 위한 기본 설정
from sqlalchemy import create_engine  # 데이터베이스 엔진 생성
from sqlalchemy.ext.declarative import declarative_base  # ORM 모델 클래스 정의를 위한 기본 클래스
from sqlalchemy.orm import sessionmaker  # 데이터베이스 세션 생성

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:1231@host.docker.internal:5432/abc"

# 데이터베이스 엔진 생성
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# 세션 팩토리 생성
# autocommit=False: 자동 커밋 비활성화 (명시적으로 commit() 호출 필요)
# autoflush=False: 자동 플러시 비활성화 (쿼리 실행 전 변경사항 자동 반영 안 함)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM 모델 클래스들이 상속받을 기본 클래스 생성
Base = declarative_base()

# 데이터베이스 세션을 생성하고 관리하는 의존성 함수
def get_db():
    db = SessionLocal()  # 새로운 데이터베이스 세션 생성
    try:
        yield db  # 세션을 호출자에게 제공
    finally:
        db.close()  # 세션 사용 후 반드시 닫기