from .Routers import post, users, authen, votes
from fastapi import *
from .oauth2 import create_token
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from . import models
from .database import get_db
from .schemas_pydantic import Post, PostResponse, Coin
from .oauth2 import get_current_user
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


origins =[
    "https://www.google.com.ng"
]


app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
 



app.include_router(post.router)
app.include_router(users.router)
app.include_router(authen.router)
app.include_router(votes.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/all", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db), current_user: models.Users = Depends(get_current_user)):
    posts = db.query(models.Post).filter(models.Post.user_id == current_user.id).all()
    # print(posts)
    return posts

@app.post("/new", status_code=status.HTTP_201_CREATED, response_model= Coin)
async def create_post(post: Coin, db: Session = Depends(get_db), current_user: models.Users = Depends(get_current_user)):
    new_post = models.Coins(**post.dict(),)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


@app.put("/new/{id}", response_model=Coin)
def update_post(id: int, post: Coin, db: Session = Depends(get_db), current_user: models.Users = Depends(get_current_user)):
    post_query = db.query(models.Coins).filter(models.Coins.id == id)
    posted = post_query.first()
    
    if posted is None:
        raise HTTPException(status_code=404, detail=f"Post with id {id} does not exist")
    
    
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    db.refresh(posted)
    
    return posted
