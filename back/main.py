# main.py
from fastapi import FastAPI
from user_controller import router as user_controller
from fastapi.middleware.cors import CORSMiddleware
from base import Base
from base import engine 
app = FastAPI()

# 애플리케이션 시작 시 데이터베이스 테이블 생성
Base.metadata.create_all(bind=engine)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],            # 허용할 도메인 목록
    allow_credentials=True,          # 쿠키를 포함한 인증 정보 허용
    allow_methods=["*"],             # 허용할 HTTP 메서드 (GET, POST 등)
    allow_headers=["*"],             # 허용할 HTTP 헤더
)

app.include_router(user_controller,tags=["user"])

        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)