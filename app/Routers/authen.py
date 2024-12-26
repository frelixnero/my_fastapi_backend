from fastapi import *
from fastapi import APIRouter, Response, Depends, status, HTTPException
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import models
from ..database import engine,get_db
from .. schemas_pydantic import TokenResponse,Login
from ..utils import verify
from  ..oauth2 import create_token, get_current_user




models.Base.metadata.create_all(bind = engine)

router = APIRouter(tags = ["Authentication"])


@router.post("/login",) #response_model=TokenResponse, tags=["authentication"])
def login_user (user_detail : OAuth2PasswordRequestForm = Depends(), db : Session = Depends(get_db),) :

    user = db.query(models.Users).filter(models.Users.email == user_detail.username).first()
    
    
    if not user :
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"invalid credentials")
    
    if not verify(user_detail.password, user.password) :
        raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"Invalid credentials")
    # print (verify(user_detail.password, user.password))
    
    access_token = create_token(data = {"user_id" : user.id})
    
    return {"access_token" : access_token, "type" : "bearer"}




# @router.post("/login",) #response_model=TokenResponse, tags=["authentication"])
# def login_user (user_detail : Login, db : Session = Depends(get_db),) :

#     user = db.query(models.Users).filter(models.Users.email == user_detail.email).first()
    
    
#     if not user :
#         raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"invalid credentials")
    
#     if not verify(user_detail.password, user.password) :
#         raise HTTPException(status_code = status.HTTP_403_FORBIDDEN, detail = f"Invalid credentials")
#     # print (verify(user_detail.password, user.password))
    
#     access_token = create_token(data = {"user_id" : user.id})
    
#     return {"access_token" : access_token, "type" : "bearer"}
    
    