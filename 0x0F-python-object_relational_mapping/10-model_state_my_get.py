#!/usr/bin/python3
"""
script that prints the State object with
the name passed as argument from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    usr, pwd, db, name = argv[1:5]
    con = "mysql+mysqldb://{}:{}@localhost/{}".format(usr, pwd, db)
    engine = create_engine(con, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == name).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    session.close()
