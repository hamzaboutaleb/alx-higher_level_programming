#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa:
"""

from sys import argv
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    usr, pwd, db = argv[1:4]
    con = "mysql+mysqldb://{}:{}@localhost/{}".format(usr, pwd, db)
    engine = create_engine(con, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco")
    new_state.cities.append(new_city)
    session.add(new_state)
    session.commit()
