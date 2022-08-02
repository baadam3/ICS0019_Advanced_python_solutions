# -*- coding: utf-8 -*-
"""
Following Python code shows how to connect to an existing database.
If the database does not exist, then it will be created and finally
a database object will be returned.
"""

import sqlite3

def opendb():
    """
    open SQLite database
    """
    global conn
    conn = sqlite3.connect('test.db')
    print ("Opened database successfully")

def create_table():
    #create a table in the previously created database
    conn.execute('''CREATE TABLE COMPANY
             (ID INT PRIMARY KEY     NOT NULL,
             NAME           TEXT    NOT NULL,
             AGE            INT     NOT NULL,
             ADDRESS        CHAR(50),
             SALARY         REAL);''')
    print ("Table created successfully")
    

def createRecords():
    """
    create some records in the COMPANY table
    """
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
                 VALUES (5, 'Paul', 32, 'California', 20000.00 )");
    
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
                 VALUES (6, 'Allen', 25, 'Texas', 15000.00 )");
    
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (7, 'Teddy', 23, 'Norway', 20000.00 )");
    
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
          VALUES (8, 'Mark', 25, 'Rich-Mond ', 65000.00 )");
    

    conn.commit()
    print ("Records created successfully")


def selectRecords():
    """
    fetch and display records from the COMPANY table
    """
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
       print ("ID = ", row[0])
       print ("NAME = ", row[1])
       print ("ADDRESS = ", row[2])
       print ("SALARY = ", row[3], "\n")
    print ("Operation done successfully")
    
def delRecords():
    """
    Delete record where ID = 7 and display records
    """
    conn.execute("DELETE from COMPANY where ID = 7;")
    conn.commit()
    print ("Total number of rows deleted :", conn.total_changes)
    
    cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
    for row in cursor:
       print ("ID = ", row[0])
       print ("NAME = ", row[1])
       print ("ADDRESS = ", row[2])
       print ("SALARY = ", row[3], "\n")
    
    print ("Operation done successfully")

def closeconn():
    """
    close connection
    """
    conn.close()
    print ("Connection closed")
    

if __name__ == "__main__":
    opendb()
#    create_table()
#    createRecords()
#    selectRecords()
    delRecords()
    closeconn()