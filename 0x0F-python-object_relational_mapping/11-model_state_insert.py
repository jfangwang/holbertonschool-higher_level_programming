#!/usr/bin/python3
"""8-model_state_fetch_first"""
import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    states_name = session.query(State.name, State.id).all()
    new_state = State()
    new_state.id = len(states_name) + 1
    new_state.name = "Louisiana"
    print(new_state.id)
    session.add(new_state)
    session.commit()
    session.close()