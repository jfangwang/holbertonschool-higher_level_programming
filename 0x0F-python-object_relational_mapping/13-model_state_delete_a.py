#!/usr/bin/python3
"""8-model_state_fetch_first"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    # You want to get the object, not the object's properties
    states_name = session.query(State).filter(State.name.like('%a%')).all()
    for a in states_name:
        session.delete(a)
    session.commit()
    session.close()
