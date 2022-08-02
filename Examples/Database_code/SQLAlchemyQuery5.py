# -*- coding: utf-8 -*-
"""
SQLAlchemy - Using query

"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
engine = create_engine('sqlite:///sales.db', echo = False)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   id = Column(Integer, primary_key =  True)
   name = Column(String)

   address = Column(String)
   email = Column(String)

Session = sessionmaker(bind = engine)
session = Session()
try:
    result = session.query(Customers).filter(Customers.id>1, Customers.id<3 )
except:
    session.rollback()
    raise
finally:
    session.close()

# The result object can be traversed using For loop to obtain 
# all records in underlying customers table
print()

for row in result:
   print ("ID: ", row.id, "Name: ",row.name, "Address:",row.address, "Email:",row.email)