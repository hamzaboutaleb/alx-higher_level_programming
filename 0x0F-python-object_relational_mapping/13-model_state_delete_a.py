#!/usr/bin/python3
"""
script that lists all State objects from the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, delete

if __name__ == "__main__":
    usr, pwd, db = argv[1:4]
    con = "mysql+mysqldb://{}:{}@localhost/{}".format(usr, pwd, db)
    engine = create_engine(con, pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.query(State).filter(State.name.like("%a%"))\
           .delete(synchronize_session=False)
    session.commit()
    session.close()
