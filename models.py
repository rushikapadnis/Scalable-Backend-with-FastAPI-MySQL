# Import Column and data types from SQLAlchemy
from sqlalchemy import Column, Integer, String

# Import Base from database.py
# Base is the parent class for all database tables
from database import Base
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key = True, index = True)
    name = Column(String(100))
    email = Column(String(100), unique = True)
    age = Column(Integer)
   # city = Column(String(50))   # 👈 NEW COLUMN
   # Degree = Column(String(50)) #new column alimbic