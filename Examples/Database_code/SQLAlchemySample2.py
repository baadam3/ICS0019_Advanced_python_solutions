# -*- coding: utf-8 -*-

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
#from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)
meta.create_all(engine)

# ins = students.insert()
ins = students.insert().values(name = 'Jüri', lastname = 'Tamm')

conn = engine.connect()
result = conn.execute(ins)


conn.execute(students.insert(), [
   {'name':'Kati', 'lastname' : 'Mets'},
   {'name':'Mati','lastname' : 'Mägi'},
   {'name':'Ants','lastname' : 'Sein'},
   {'name':'Mari','lastname' : 'Kivi'},
])

conn.close()