# -*- coding: utf-8 -*-
"""
SQLAlchemy - Updating Objects
"""

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key =  True)
   name = Column(String)

   address = Column(String)
   email = Column(String)

engine = create_engine('sqlite:///sales.db', echo = True)

Session = sessionmaker(bind = engine)
session = Session()

try:
    x = session.query(Customers).get(2)
    print ("Name: ", x.name, "Address:", x.address, "Email:", x.email)
    x.address = 'Kohila'
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()