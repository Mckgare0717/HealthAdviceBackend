from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from api import Users


app =FastAPI()
origins = [
    "http://localhost",
    "http://localhost:3000",
    "https://localhost",
    "https://localhost:3000",
    "*"# Assuming your React app runs on port 3000
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(Users.router,prefix="/users",tags=["users"])
@app.get("/")
def welcmePg():
    return{"welcome to my page"}
