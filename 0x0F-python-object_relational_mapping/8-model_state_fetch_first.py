#!/usr/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    firstState = session.query(State).order_by(State.id).first()

    if firstState != None:
        print("{}: {}".format(firstState.id, firstState.name))
    else:
        print("Nothing")
    session.close()
