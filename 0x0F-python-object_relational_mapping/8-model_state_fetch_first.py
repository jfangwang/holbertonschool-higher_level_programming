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
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states_name = session.query(State).order_by(State.id).first()
    try:
        print("{}: {}".format(states_name.id, states_name.name))
    except:
        print("Nothing")
    session.close()
