#!/usr/bin/python3
'''
A script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
'''
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == '__main__':
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City).order_by(City.id).all()

    for city in cities:
        state_name = city.state.name if city.state else "N/A"
        print(f"{city.id}: {city.name} -> {state_name}")

    session.close()
