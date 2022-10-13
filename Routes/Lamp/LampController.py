from http.client import HTTPException

from fastapi import APIRouter

from Models.LampModel import LampModel

lampRouter = APIRouter(
    prefix="/lamp"
)

listOfLamp =[]

@lampRouter.get("/all")
async def getAllLamp():
    return listOfLamp

@lampRouter.get("/{id}")
async def getLampByID(id: int):
    for lamp in listOfLamp:
        if lamp.id == id:
            return lamp
    raise HTTPException(status_code=404, detail="Data is not available")
@lampRouter.post("/create")
async def createNewLamp(lampModel: LampModel):
    listOfLamp.append(lampModel)
    return {
        "success": True,
        "message": "success",
        "code": 200
    }
@lampRouter.put("/update")
async def updateLamp(lampModel: LampModel):
    for i in range (len(listOfLamp) - 1):
        if listOfLamp[i].id == lampModel.id:
            listOfLamp[i] = lampModel
    return {
        "success": True,
        "message": "success",
        "code": 200
    }

@lampRouter.delete("/delete/{id}")
async def deleteLamp(id: int):
    # nge delete ceunah
    return {
        "success": True,
        "message": "success",
        "code": 200
    }