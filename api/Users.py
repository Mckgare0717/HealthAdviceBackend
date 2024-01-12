from fastapi import FastAPI, HTTPException,APIRouter
from pydantic import BaseModel
from schemas.utils import getUser,saveUser
import uuid 
import jwt


router = APIRouter()
SECRET_KEY = "HealthAdvice"

class AuthCreds(BaseModel):
    name:str
    email:str
    password:str = None
    
class Login(BaseModel):
    email:str
    password:str
    
class LoginResponse(BaseModel):
    name:str
    email:str
    id:str
    token:str

@router.post("/register")
async def newUser(creds:AuthCreds):
    users = getUser()
    
    
    for user in users["users"]:
        if creds.email == user["email"]:
            raise HTTPException(status_code=400,detail="Email already registered.")

    id = str(uuid.uuid1())
    tokenID = {"sub":id}
    token  = jwt.encode(tokenID,SECRET_KEY,algorithm="HS256")
        
    userNew = {
        "id" : id,
        "name":creds.name,
        "email": creds.email,
        "password":creds.password,
        "access_token":token
    }
        
    
        
    users["users"].append(userNew)
    saveUser(users)
    return userNew
    


@router.post("/login")
async def loginUser(user:Login):
    users = getUser()
    
    for u in users["users"]:
        print(users["users"])
        print(u["email"])
        if u["email"] == user.email and u["password"]==user.password:
            return u
        
    raise HTTPException(status_code=400,detail="Incorrect credentials")
        
