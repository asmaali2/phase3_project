# db.py

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///mydatabase.db', echo=True)
Session = sessionmaker(bind=engine)

def create_tables():
    BaseException.metadata.create_all(engine)
