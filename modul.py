from datetime.datetime import 
from sqlalchemy import (Column, Integer, String, Boolean, Text, Date, ForeignKey, create_engine)
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///app.db', echo=True)
Base = declarative_base(bind=engine)

class Abstract():
    id = Column(Integer, primery_key=True)
    created_on = Column(Date, default=)

class User(Base):
