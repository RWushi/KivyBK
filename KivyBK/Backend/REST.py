from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn
from Backend.Config import session
from Backend.DB.Models import User
from sqlalchemy import select


app = FastAPI()


class LocationData(BaseModel):
    latitude: float
    longitude: float


@app.post("/location/")
async def location(data: LocationData):
    latitude = data.latitude
    longitude = data.longitude

    async with session() as s:
        user = await s.scalar(select(User).where(User.id == 1))
        user.latitude = latitude
        user.longitude = longitude
        await s.commit()


if __name__ == "__main__":
    uvicorn.run("Backend.REST:app", port=8080, reload=True)
