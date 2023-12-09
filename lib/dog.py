

from models import Dog
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Base, Dog

def create_table(base):
    engine = create_engine('sqlite:///dogs.db', echo=True)  # Replace with your actual database connection
    base.metadata.create_all(bind=engine)

def save(session, dog):
    session.add(dog)
    session.commit()

def get_all(session):
    return session.query(Dog).all()

def find_by_name(session, name):
    return session.query(Dog).filter(Dog.name == name).first()

def find_by_id(session, dog_id):
    return session.query(Dog).get(dog_id)

def find_by_name_and_breed(session, name, breed):
    return session.query(Dog).filter(Dog.name == name, Dog.breed == breed).first()

def update_breed(session, dog, new_breed):
    dog.breed = new_breed
    session.commit()

engine = create_engine('sqlite:///:memory:', echo=True)

# Bind the engine to the Base class
Base.metadata.bind = engine

# Create tables
Base.metadata.create_all()

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Example usage of functions
dog1 = Dog(name='Buddy', breed='Golden Retriever')
save(session, dog1)

all_dogs = get_all(session)
print(all_dogs)

found_dog = find_by_name(session, 'Buddy')
print(found_dog)

session.close()