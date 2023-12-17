#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format(
                        sys.argv[1], sys.argv[2],
                        sys.argv[3]), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(engine)
    session = Session()

    found = 0
    for state in session.query(State).order_by(State.id).all():
        if sys.argv[4] == state.name:
            print("{}: {}".format(state.id, state.name))
            found = 1
    if found == 0:
        print("Not found")
    session.close()
