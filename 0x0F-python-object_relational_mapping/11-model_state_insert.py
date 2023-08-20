#!/usr/bin/python3
"""
cript that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    usr, pwd, db = argv[1:4]
    con = "mysql+mysqldb://{}:{}@localhost/{}".format(usr, pwd, db)
    engine = create_engine(con, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="Louisiana")
    session.add(state)
    session.commit()

    print(state.id)
    session.close()
