from fastapi import APIRouter, Depends, HTTPException, status
from typing import List, Optional
from sqlalchemy.orm import Session
from .. import models
from ..database import get_db
from ..schemas_pydantic import Post, PostResponse
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]
)

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=PostResponse)
async def create_post(post: Post, db: Session = Depends(get_db), current_user: models.Users = Depends(get_current_user)):
    new_post = models.Post(**post.dict(), user_id=current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post





@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int, db: Session = Depends(get_db), current_user: models.Users = Depends(get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    if post_query.first() is None:
        raise HTTPException(status_code=404, detail="Post does not exist")
    post = post_query.first()
    if post.user_id != current_user.id :
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "User cannot perform this action")
    
    post_query.delete(synchronize_session=False)
    db.commit()


@router.put("/{id}", response_model=PostResponse)
def update_post(id: int, post: Post, db: Session = Depends(get_db), current_user: models.Users = Depends(get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    posted = post_query.first()
    
    if posted is None:
        raise HTTPException(status_code=404, detail=f"Post with id {id} does not exist")
    
    if posted.user_id != current_user.id :
        raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "User cannot perform this action")
    
    print(posted)
    print(f"Post query {post.dict()}")
    post_query.update(post.dict(), synchronize_session=False)
    db.commit()
    db.refresh(posted)
    
    return posted




@router.get("/", response_model=List[PostResponse])
def get_posts(db: Session = Depends(get_db), current_user: models.Users = Depends(get_current_user), limit : int = 10, skip : int = 0, search : Optional[str] = ""):
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    print(limit)
    return posts




# @router.get("/all", response_model=List[PostResponse])
# def get_posts(db: Session = Depends(get_db), current_user: models.Users = Depends(get_current_user)):
#     posts = db.query(models.Post).filter(models.Post.user_id == current_user.id).all()
#     return posts


@router.get("/{id}", response_model=PostResponse)
async def get_post(id: int, db: Session = Depends(get_db), current_user: models.Users = Depends(get_current_user)):
    post = db.query(models.Post).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'post with id {id} was not found')
        
    # if post.user_id != current_user.id :
    #     raise HTTPException(status_code = status.HTTP_401_UNAUTHORIZED, detail = "User cannot perform this action")
    
    return post
