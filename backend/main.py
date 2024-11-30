from fastapi import FastAPI
from api.user_registration import router as registration_router
from api.user_recommendations import router as recommendation_router
from api.user_journey import router as journey_router
from api.add_to_shelf import router as add_to_shelf_router
from api.reading_gorgress import router as reading_grogres_router
from api.user_shelf import router as user_shelf_router
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
app.include_router(add_to_shelf_router, tags=["add_to_shelf"])
app.include_router(reading_grogres_router, tags=["reading_gorgress"])
app.include_router(user_shelf_router, tags=["user_shelf"])

@app.get("/")
async def root():
    return {"message": "Welcome to SkyShelf!"}
