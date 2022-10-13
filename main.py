from fastapi import FastAPI

from Routes.Auth.AuthController import authRouter
from Routes.Lamp.LampController import lampRouter

app = FastAPI()
app.include_router(authRouter)
app.include_router(lampRouter)
@app.get("/")
async def root():
    return {"message": "Hello World"}
