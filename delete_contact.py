from database import SessionLocal
from models import Contact

session = SessionLocal()
contact = session.query(Contact).filter_by(id=2).first()

if contact:
    session.delete(contact)
    session.commit()
    print("Contact deleted permanently.")
else:
    print("Contact not found.")
