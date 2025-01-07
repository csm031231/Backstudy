# main.py
from fastapi import FastAPI
from user_controller import router as user_controller


app = FastAPI()

app.include_router(user_controller,tags=["user"])

        
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)