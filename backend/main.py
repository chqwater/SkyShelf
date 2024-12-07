from fastapi import FastAPI
from api.user_registration import router as registration_router
from api.user_recommendations import router as recommendation_router
from api.user_journey import router as journey_router
from api.add_to_shelf import router as add_to_shelf_router
from api.reading_gorgress import router as reading_grogres_router
from api.user_shelf import router as user_shelf_router
from api.edit_book import router as edit_book_router
from api.admin_users import router as admin_users_router
from api.user_login import router as login_router
from api.user_password_change import router as password_change_router
from api.admin_books import router as admin_books_router
from api.admin_delete_book import router as delete_book_router
from api.admin_create_book import router as create_book_router
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
app.include_router(admin_users_router, tags=["admin_users"])
app.include_router(edit_book_router, tags=["edit_book"])
app.include_router(login_router, tags=["login"])
app.include_router(password_change_router, tags=["new_password"])
app.include_router(admin_books_router, tags=["admin_books"])
app.include_router(delete_book_router, tags=["delete_book"])
app.include_router(create_book_router,tags=["create_book"])

@app.get("/")
async def root():
    return {"message": "Welcome to SkyShelf!"}
