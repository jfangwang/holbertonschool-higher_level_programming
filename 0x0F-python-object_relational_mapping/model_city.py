#!/usr/bin/python3
"""model_state"""
from sqlalchemy import create_engine, Column, Integer, String
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
# Base = declarative_base()


class City(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, auto_increment = True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, )

# if __name__ == "__main__":
#     engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'\
#                             .format(sys.argv[1], sys.argv[2], sys.argv[3]))
#     Base.metadata.create_all(engine)
#     Session = sessionmaker(bind=engine)
#     session = Session()
#     session