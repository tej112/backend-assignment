from typing import List
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import desc
from sqlalchemy.orm import Session
from . import models, schemas
from .database import engine, SessionLocal
import requests

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def root():
    return {"message": "Hello World"}


@app.get("/api/users/")
def get_users(page: int = 1, limit: int = 5, name: str = None, sort: str = None, db: Session = Depends(get_db)):
    if name:
        if sort:
            if sort[0] == "-":
                users = db.query(models.User).filter(models.User.first_name.ilike(f"%{name}%")).order_by(desc(sort[1:])).offset((page - 1) * limit).limit(limit).all()
            else:
                users = db.query(models.User).filter(models.User.first_name.ilike(f"%{name}%")).order_by(sort).offset((page - 1) * limit).limit(limit).all()
        else:
            users = db.query(models.User).filter(models.User.first_name.ilike(f"%{name}%")).offset((page - 1) * limit).limit(limit).all()
    else:
        if sort:
            if sort[0] == "-":
                users = db.query(models.User).order_by(desc(sort[1:])).offset((page - 1) * limit).limit(limit).all()
            else:
                users = db.query(models.User).order_by(sort).offset((page - 1) * limit).limit(limit).all()
        else:
            users = db.query(models.User).offset((page - 1) * limit).limit(limit).all()
    return users


@app.post("/api/users/", status_code=201)
def create_user(user: schemas.User, db: Session = Depends(get_db)):
    is_user = db.query(models.User).filter(models.User.id == user.id).first() 

    if is_user:
        raise HTTPException(status_code=400, detail="User already exists")

    db_user = models.User(**user.dict())

    db.add(db_user)
    db.commit()

    return {}


@app.get("/api/users/{id}/", status_code=200, response_model=schemas.User)
def get_user(id: int, db: Session = Depends(get_db)):

    user = db.query(models.User).filter(models.User.id == id).first()

    if not user:

        raise HTTPException(status_code=404, detail="User not found")

    return user.dict()


@app.put("/api/users/{id}/", status_code=200, response_model=schemas.UserUpdate)
def update_user(id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(models.User.id == id).first()

    if not db_user:

        raise HTTPException(status_code=404, detail="User not found")

    for key, value in user.dict().items():

        if value is not None and not value == "string" and not value == 0 and not value == "":

            setattr(db_user, key, value)

    db.commit()

    return {}


@app.delete("/api/users/{id}/", status_code=200)
def delete_user(id: int, db: Session = Depends(get_db)):

    db_user = db.query(models.User).filter(models.User.id == id).first()

    if not db_user:

        raise HTTPException(status_code=404, detail="User not found")

    db.delete(db_user)
    db.commit()

    return {}
    
@app.post("/populateDB/")
def create_user(db: Session = Depends(get_db)):
    url = "https://datapeace-storage.s3-us-west-2.amazonaws.com/dummy_data/users.json"

    for user in requests.get(url).json():

        db_user = models.User(**user)
        db.add(db_user)
    db.commit()

    return {"message": "Successfully populated database"}