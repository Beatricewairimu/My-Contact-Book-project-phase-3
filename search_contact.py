from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Contact(Base):
    __tablename__ = 'contacts'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

# Database setup
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

def search_by_letter(letter):
    results = session.query(Contact).filter(Contact.name.ilike(f"{letter}%")).order_by(Contact.name).all()
    if results:
        print("\nMatching Contacts:")
        for i, contact in enumerate(results, 1):
            print(f"{i}. {contact.name}")
        
        choice = input("\nSelect a contact number to view details (or 0 to cancel): ").strip()
        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(results):
                selected_contact = results[choice - 1]
                print(f"\nContact Details:\nName: {selected_contact.name}\nPhone: {selected_contact.phone}\nEmail: {selected_contact.email}")
            elif choice == 0:
                print("Cancelled.")
            else:
                print("Invalid choice.")
        else:
            print("Invalid input.")
    else:
        print("No contacts found.")

if __name__ == "__main__":
    add_contact("Beatrice Wairimu", "0793625311", "wairimubeatrice209@gmail.com")
    add_contact("Maya Kinyanjui", "0723835621", "mayakinyanjui19@gmail.com")
    add_contact("Brian Karanja", "0712345678", "briankaranja5@gmail.com")
    add_contact("Mary Wambui", "0723445564", "marywambui9@gmail.com")
    add_contact("maya kinyanjui", "0722394442", "mayakinyanjui19@gmail.com")

    letter = input("\nEnter the first letter to search contacts: ").strip().lower()
    search_by_letter(letter)

