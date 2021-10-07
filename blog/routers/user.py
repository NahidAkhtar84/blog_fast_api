from fastapi import APIRouter
from .. import schemas, database, oauth2
from sqlalchemy.orm import Session
from fastapi import FastAPI, Depends
from ..repository import user

router = APIRouter(
    prefix='/user',
    tags=['Users']
)
get_db = database.get_db


# User
@router.post('/', status_code=201, response_model=schemas.ShowUser)
def user_create(request: schemas.User, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return user.create(request, db)

@router.get('/{id}', status_code=200, response_model=schemas.ShowUser)
def show_user(id: int, db: Session = Depends(get_db), current_user: schemas.User= Depends(oauth2.get_current_user)):
    return user.show_user(id, db)
