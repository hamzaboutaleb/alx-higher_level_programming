#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa:
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    usr, pwd, db = argv[1:4]
    con = "mysql+mysqldb://{}:{}@localhost/{}".format(usr, pwd, db)
    engine = create_engine(con, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    cities_states = session.query(State, City)\
                           .filter(State.id == City.state_id)\
                           .order_by(City.id).all()
    for city, state in cities_states:
        print("{}: ({}) {}".format(city.name, state.id, state.name))
    session.close()
