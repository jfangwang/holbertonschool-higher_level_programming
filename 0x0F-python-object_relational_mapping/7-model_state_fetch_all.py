#!/usr/bin/python3
"""7-model_state_fetch"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    states_name = session.query(State).order_by(State.id).all()
    for a in states_name:
        print("{}: {}".format(a.id, a.name))
    session.close()
