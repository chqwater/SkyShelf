from fastapi import FastAPI
from api.user_registration import router as registration_router
from api.user_recommendations import router as recommendation_router
from api.user_journey import router as journey_router
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = [
    "http://127.0.0.1:5173",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(registration_router, tags=["registration"])
app.include_router(recommendation_router, tags=["recommendation"])
app.include_router(journey_router, tags=["journey"])

@app.get("/")
async def root():
    return {"message": "Welcome to SkyShelf!"}
