
from pydantic import BaseModel 

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

class UserResponse(UserCreate):
    id: int 
    class Config:
        orm_mode = True #without this pydentic ignore orm attribute
        
