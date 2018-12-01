import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from data_layer.tabledef import *

engine = create_engine('sqlite:///users.db', echo=True)

# create a Session
Session = sessionmaker(bind=engine)
session = Session()

user = User("admin", "password", "Chirag", "Awale","cawaleinfo@gmail.com", "##########")
session.add(user)

user = User("python", "python", "test", "test","test@test.com", "##########")
session.add(user)

user = User("jumpiness", "python", "test", "test","test@test.com", "##########")
session.add(user)

# commit the record the database
session.commit()

session.commit()