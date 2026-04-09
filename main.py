from fastapi import FastAPI, Depends, HTTPException, Response, status
from sqlalchemy.orm import Session
import schemas
from dependencies import get_db

from database import engine
import models

app = FastAPI()

#models.Base.metadata.create_all(bind= engine)

@app.post("/users", response_model = schemas.UserResponse, status_code = status.HTTP_201_CREATED)
def create_user(user:schemas.UserCreate, db:Session = Depends(get_db)):
    db_user = models.User(
        name=user.name,
        email=user.email,
        age=user.age,
        
    )
    db.add(db_user)
    db.commit()

    db.refresh(db_user)

    return db_user

@app.get("/users", response_model =list[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.put("/users/{user_id}") #Put /user/ 3
def update_user(user_id: int, user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code = 404, detail ="user not found ")
    db_user.name = user.name
    db_user.email = user.email
    db_user.age = user.age

    db.commit()
    db.refresh(db_user) # this reload the refresh value from db before written 
    return db_user 

@app.delete("/users/{user_id}", status_code = status.HTTP_204_NO_CONTENT)
def delete_user(user_id:int, db: Session= Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if not db_user:
        raise HTTPException(status_code = 404 , detail = "user  not found")
    
    db.delete(db_user)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)
