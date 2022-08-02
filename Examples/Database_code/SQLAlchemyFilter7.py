# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 21:16:51 2019

@author: eikivi
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy import or_

engine = create_engine('sqlite:///sales.db', echo = False)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   
   id = Column(Integer, primary_key = True)
   name = Column(String)

   address = Column(String)
   email = Column(String)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind = engine)
session = Session()

try:
#    result = session.query(Customers).filter(or_(Customers.id>2, Customers.name.like('Ei%')))
    #result = session.query(Customers).filter(Customers.id<2, Customers.name.like('Ja%'))
    result = session.query(Customers).filter(Customers.id != 2)
    #result = session.query(Customers).one()
except:
    session.rollback()
    raise
finally:
    session.close()

print("")
#print(result)

for row in result:
   print("")
   print ("ID:", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)