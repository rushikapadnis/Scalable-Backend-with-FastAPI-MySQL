from database import SessionLocal

# This function creates a database session
def get_db():
    db = SessionLocal()   # Open database connection
    try:
        yield db          # Give the DB session to API
    finally:
        db.close()        # Always close DB after request
