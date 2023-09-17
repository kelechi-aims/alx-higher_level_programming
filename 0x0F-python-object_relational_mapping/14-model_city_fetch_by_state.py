#!/usr/bin/python3
'''
A script that that prints all City objects from the database hbtn_0e_6_usa
You must use the module SQLAlchemy
'''
from sys import argv
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(City, State).filter(
        City.state_id == State.id).order_by(City.id).all()

    for city, state in cities:
        print(f"{state.name}: ({city.id}) {city.name}")

    session.close()
