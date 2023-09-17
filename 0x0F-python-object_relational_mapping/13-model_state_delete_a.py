#!/usr/bin/python3
'''
A script that deletes all State objects with a name containing the letter a
from the database hbtn_0e_6_usa
You must use the module SQLAlchemy
'''
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    db_url = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)
    session = Session()

    deleting_states = session.query(State).filter(State.name.like('%a%')).all()

    for state in deleting_states:
        session.delete(state)
    session.commit()

    session.close()
