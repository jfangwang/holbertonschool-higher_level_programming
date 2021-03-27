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

    # Check for injections
    argv = sys.argv
    index = 0
    while argv[4][index].isalpha() and index < len(argv[4]) - 1:
        index += 1
    if argv[4][index].isalpha():
        index += 1
    argv[4] = argv[4][slice(index)]

    Session = sessionmaker(bind=engine)
    session = Session()
    states_name = session.query(State)\
        .filter(State.name.like(sys.argv[4])).first()
    try:
        print(states_name.id)
    except:
        print("Not found")
    session.close()
