from pydantic import BaseModel

class LampModel(BaseModel):
    id: int
    state: bool
    brightness: int