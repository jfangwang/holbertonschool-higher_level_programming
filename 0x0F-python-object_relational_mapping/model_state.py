#!/usr/bin/python3
"""model_state"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True)
    name = Column(String(128), nullable=False)

# Realized this file was meant to be importing a class only
# if __name__ == "__main__":
#     engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
#                             .format(sys.argv[1], sys.argv[2], sys.argv[3]))
#     Base.metadata.create_all(engine)
