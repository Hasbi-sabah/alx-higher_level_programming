#!/usr/bin/python3
'''
A script that lists all State objects, and corresponding City objects,
contained in a databas
'''
from sqlalchemy import create_engine
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy.orm import sessionmaker

from sys import argv

if __name__ == "__main__":
    engine = create_engine(f"mysql://{argv[1]}:{argv[2]}@\
localhost:3306/{argv[3]}")
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).join(State).all()
    prev_state = ""
    for cities, states in query:
        if states.name is not prev_state:
            prev_state = states.name
            print(f"{states.id}: {states.name}")
        print(f"    {cities.id}: {cities.name}")
    session.close()
