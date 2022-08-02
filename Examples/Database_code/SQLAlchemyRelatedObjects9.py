# -*- coding: utf-8 -*-
"""
SQLAlchemy - Working with related Objects
"""

from sqlalchemy import create_engine, ForeignKey, Column, Integer, String
engine = create_engine('sqlite:///sales.db', echo = True)
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

class Customer(Base):
   __tablename__ = 'customers'

   id = Column(Integer, primary_key = True)
   name = Column(String)
   address = Column(String)
   email = Column(String)

class Invoice(Base):
   __tablename__ = 'invoices'
   
   id = Column(Integer, primary_key = True)
   custid = Column(Integer, ForeignKey('customers.id'))
   invno = Column(Integer)
   amount = Column(Integer)
   customer = relationship("Customer", back_populates = "invoices")


Customer.invoices = relationship("Invoice", order_by = Invoice.id, back_populates = "customer")

c1 = Customer(name = "Jüri Ratas", address = "Toompea, Tallinn", 
              email = "jyri.ratas@valitsus.ee" ,
              invoices = [Invoice(invno = 10, amount = 15000), 
                          Invoice(invno = 14, amount = 3850)])


Session = sessionmaker(bind = engine)
session = Session()

try:
    session.add(c1)
    session.commit()
except:
    session.rollback()
    raise
finally:
    session.close()