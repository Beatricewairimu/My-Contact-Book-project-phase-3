from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

# This is to set up the DataBase
engine = create_engine('sqlite:///contacts.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def add_contact(name, phone, email):
    existing_contact = session.query(Contact).filter_by(name=name, phone=phone, email=email).first()
    
    if existing_contact:
        print(f"Contact {name} already exists.")
    else:
        contact = Contact(name=name, phone=phone, email=email)
        session.add(contact)
        session.commit()
        print(f"Contact {name} added.")

def get_contacts():
    print("Fetching contacts...")
    contacts = session.query(Contact).all()
    if contacts:
        for contact in contacts:
            print(f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
    else:
        print("No contacts found.")
    input("Press Enter to continue...")  # Pause fSor user to seeS contacts

def delete_contact(contact_id):
    contact = session.query(Contact).filter_by(id=contact_id).first()
    if contact:
        session.delete(contact)
        session.commit()
        print(f"Contact {contact_id} deleted.")
    else:
        print("Contact not found.")

def cli_menu():
    while True:
        print("\n--- Contact Book CLI Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        print("5. Search Contact")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif choice == '2':
            print("Fetching contacts...")
            contacts = session.query(Contact).all()
            if contacts:
                for contact in contacts:
                    print(f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
            else:
                print("No contacts found.")
            input("Press Enter to continue...")  # Pause for user to see contacts
        elif choice == '3':
            contact_id = int(input("Enter contact ID to delete: "))
            delete_contact(contact_id)
        elif choice == '4':
            print("Exiting the program.")
            break
        elif choice == '5':
            name = input("Enter name to search: ")
            search_contact(name)
        else:
            print("Invalid choice. Please try again.")

def search_contact(name):
    contacts = session.query(Contact).filter(Contact.name.contains(name)).all()
    if contacts:
        for contact in contacts:
            print(f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
    else:
        print("No contacts found with that name.")

# Start the CLI menu
if __name__ == "__main__":
    cli_menu()
