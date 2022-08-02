# -*- coding: utf-8 -*-
"""
complete script to add a record in customers table
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///sales.db', echo = True)

Base = declarative_base()

class Customers(Base):
   __tablename__ = 'customers'
   
   id = Column(Integer, primary_key=True)
   name = Column(String)
   address = Column(String)
   email = Column(String)

Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()
try:
    c1 = Customers(name = 'Einar Kivisalu', address = 'Raja 4C, Tallinn', email = 'eikivi@ttu.ee')
    
    session.add(c1)
    
    session.add_all([
       Customers(name = 'Kalle Tammemäe', address = 'Tallinn, Raja 4c', email = 'mingi@mail.ee'), 
       Customers(name = 'Jaak Aaviksoo', address = 'Ehitajate tee 5', email = 'jaak@ttu.ee')]
    )
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()
