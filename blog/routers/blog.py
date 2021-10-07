from fastapi import APIRouter
from typing import List
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends, status, Response, HTTPException
from ..repository import blog


router = APIRouter(
    prefix='/blog',
    tags=['Blogs']
)
get_db = database.get_db


@router.get('/', response_model=List[schemas.ShowBlog])
def get_all_blogs(db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.get_all(db)



@router.post('/', status_code=201)
def create(request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.create(request, db)



@router.get('/{id}', status_code=200, response_model=schemas.ShowBlog)
def show_one_blog(id, response: Response, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.show_one(id, db)

@router.delete('/{id}', status_code=204)
def destroy(id, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Blog, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return blog.update(id, request, db)

