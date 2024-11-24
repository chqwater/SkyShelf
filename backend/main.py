from fastapi import FastAPI
from api.user_registration import router as registration_router
from api.user_recommendations import router as recommendation_router
from api.user_journey import router as journey_router

app = FastAPI()

# Include routers
app.include_router(registration_router, prefix="/registration", tags=["registration"])
app.include_router(recommendation_router, prefix="/recommendation", tags=["recommendation"])
app.include_router(journey_router, prefix="/journey", tags=["journey"])

@app.get("/")
async def root():
    return {"message": "Welcome to SkyShelf!"}
