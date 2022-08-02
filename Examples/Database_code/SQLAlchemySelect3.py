# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:08:58 2019

@author: eikivi
"""

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
engine = create_engine('sqlite:///college.db', echo = True)
meta = MetaData()

students = Table(
   'students', meta, 
   Column('id', Integer, primary_key = True), 
   Column('name', String), 
   Column('lastname', String), 
)

#s = students.select()
s = students.select().where(students.c.id<4)

conn = engine.connect()
result = conn.execute(s)

print()
for row in result:
   print (row)
   
conn.close()   