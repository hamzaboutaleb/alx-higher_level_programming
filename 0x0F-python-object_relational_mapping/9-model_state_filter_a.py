#!/usr/bin/python3
"""
script that lists all State objects that
contain the letter a from the database hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    usr, pwd, db = argv[1:4]
    con = "mysql+mysqldb://{}:{}@localhost/{}".format(usr, pwd, db)
    engine = create_engine(con, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    states = session.query(State).filter(State.name.like("%a%"))\
                    .order_by(State.id).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))
    session.close()
