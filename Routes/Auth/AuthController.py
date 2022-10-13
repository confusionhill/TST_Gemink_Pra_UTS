from fastapi import APIRouter
from Models.AuthModel import UserModel

authRouter = APIRouter()
listOfUsers = []

def authenticateUser(model: UserModel):
    return {
        "token": "ffe38c9742af123f5151bb57b8594c868517ac5723a7c8c5dc1799f17bf05454",
        "user_id": 1
    }

@authRouter.post("/register")
async def registerUser(model: UserModel):
    # register user
    # FAKE ACTION.........
    listOfUsers.append(model)
    return authenticateUser(model)
@authRouter.get("/login")
async def loginUser(model: UserModel):
    # validate user
    for user in listOfUsers:
        if user.email == model.email and model.password == user.password:
            return authenticateUser(model)
    return {}

@authRouter.get("/all")
async def getReistered():
    return listOfUsers