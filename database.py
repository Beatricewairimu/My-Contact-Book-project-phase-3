from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base

# Create the database engine
engine = create_engine("sqlite:///contacts.db")  # SQLite database

# Create the tables in the database
Base.metadata.create_all(engine)

# Create a session factory
SessionLocal = sessionmaker(bind=engine)
