#!/usr/bin/python3
'''
A script that changes the name of a State object
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

    updating_state = session.query(State).filter_by(id=2).first()
    if updating_state:
        updating_state.name = 'New Mexico'
        session.commit()

    session.close()
