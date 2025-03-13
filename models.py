from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True, autoincrement=True)  # Ensure AUTOINCREMENT
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Set up the database
engine = create_engine('sqlite:///contacts.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
