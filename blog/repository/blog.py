from sqlalchemy.orm import Session
from .. import models
from fastapi import FastAPI, Depends, status, HTTPException

def get_all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, creator_id=request.creator_id)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

def show_one(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        #         response.status_code = status.HTTP_404_NOT_FOUND
        #         return {'detail': f"The blog with the id: {id} is not available"}
        raise HTTPException(status_code=404, detail=f"The blog with the id: {id} is not available")
    return blog

def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog of id: {id} is not found")
    blog.delete(synchronize_session=False)
    db.commit()
    return {'detail': 'The instance has been deleted!'}

def update(id: int, request, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"The blog of id: {id} is not found")
    blog.update({models.Blog.title: request.title, models.Blog.body: request.body}, synchronize_session=False)
    db.commit()
    return "the data has been updated!"