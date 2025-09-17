from fastapi import FastAPI, Depends, HTTPException, status, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from typing import List
from contextlib import asynccontextmanager

from .Routers import post, users, authen, votes
from .oauth2 import create_token, get_current_user
from . import models
from .database import get_db
from .schemas_pydantic import Post, PostResponse, Coin

# Define the FastAPI app with lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup tasks
    print("Application starting...")
    yield
    # Shutdown tasks
    print("Application shutting down...")

app = FastAPI(lifespan=lifespan)

# CORS setup
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(post.router)
app.include_router(users.router)
app.include_router(authen.router)
app.include_router(votes.router)

# Root route
@app.get("/")
async def root():
    return {"message": "Hello World"}

# Get all posts
@app.get("/all", response_model=List[PostResponse])
def get_posts(
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    posts = db.query(models.Post).filter(models.Post.user_id == current_user.id).all()
    return posts

# Create a new post
@app.post("/new", status_code=status.HTTP_201_CREATED, response_model=Coin)
async def create_post(
    post: Coin,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    new_post = models.Coins(**post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post

# Update a post
@app.put("/new/{id}", response_model=Coin)
def update_post(
    id: int,
    post: Coin,
    db: Session = Depends(get_db),
    current_user: models.Users = Depends(get_current_user),
):
    post_query = db.query(models.Coins).filter(models.Coins.id == id)
    posted = post_query.first()

    if posted is None:
        raise HTTPException(status_code=404, detail=f"Post with id {id} does not exist")

    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    db.refresh(posted)

    return posted
