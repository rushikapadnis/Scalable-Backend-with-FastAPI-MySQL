# Import create_engine:
# This is used to create a connection between FastAPI and the database
from sqlalchemy import create_engine

# sessionmaker → creates database sessions
# declarative_base → base class for all ORM models (tables)
from sqlalchemy.orm import sessionmaker, declarative_base


# Database connection URL
# Format:
# mysql+pymysql://username:password@host/database_name
#DATABASE_URL = "mysql+pymysql://root:123456@localhost/fastapi_db"
DATABASE_URL = "mysql+pymysql://root:123456@127.0.0.1/fastapi_db"



# engine is the actual connection to the database
# Think of engine as: "FastAPI ka DB plug"
engine = create_engine(DATABASE_URL)


# SessionLocal is used to talk to the database
# Every API request will get its own DB session
SessionLocal = sessionmaker(
    autocommit=False,   # We will manually save data
    autoflush=False,    # Changes won't auto-save
    bind=engine         # Session will use this engine
)


# Base is the parent class for all database models
# Every table class will inherit from Base
Base = declarative_base()
try:
    connection = engine.connect()
    print("✅ Database connected successfully!")
    connection.close()
except Exception as e:
    print("❌ Connection failed:", e)