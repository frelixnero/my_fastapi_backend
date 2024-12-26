from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from pydantic.types import conint

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    
    class Config:
        orm_mode = True
        
class UserOut(BaseModel):
    id: int
    email: EmailStr
    time_created: datetime

    class Config:
        orm_mode = True

class PostResponse(Post):
    title: str
    content: str
    published: bool
    id : int
    user_id: int
    
    owner : UserOut

    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str



class Login(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[int] = None


 
class Coin(BaseModel) :
    coin_amount : int 
    
    
class Vote(BaseModel) :
    post_id : int
    dir : int