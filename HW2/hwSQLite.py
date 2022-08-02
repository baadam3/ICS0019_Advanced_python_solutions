'''
This python file contains functions necesarry to connect to a database.
If the given database does not exist, it will be created!
'''
import sqlite3

def opendb():
    """
    innitiates connection to database diners
    """
    global conn
    conn = sqlite3.connect('diners.db')
    print ("Opened database successfully")

def createTable():
    #creates tables PROVIDER and CANTEEN in diners.db
    try:
        conn.execute('''CREATE TABLE PROVIDER
                (ID                    INT     NOT NULL,
                ProviderName           TEXT    NOT NULL,
                PRIMARY KEY (ID));''')
        print ("Table provider created successfully")

        conn.execute('''CREATE TABLE CANTEEN
                (ID            INT    NOT NULL,
                ProviderID     INT    NOT NULL,
                Name           TEXT   NOT NULL,
                Location       CHAR(50),
                time_open      INT,
                time_closed    INT,
                PRIMARY KEY (ID),
                FOREIGN KEY (ProviderID) REFERENCES PROVIDER(ID));''')
        print ("Table canteen created successfully")
    except:
        print("Tables were not created, they either already exist or there were some errors!")

def createRecords():
    """
    create some records in the CANTEEN and PROVIDER tables
    """
    try:
        #Adds records to provider table
        conn.execute('''INSERT INTO PROVIDER (ID,ProviderName)
        VALUES (1, "Rahva Toit")''')

        conn.execute('''INSERT INTO PROVIDER (ID, ProviderName)
        VALUES (2, "Baltic Restaurants Estonia AS");''')

        conn.execute('''INSERT INTO PROVIDER (ID, ProviderName)
        VALUES (3, "TTÜ Sport OÜ");''')

        conn.execute('''INSERT INTO PROVIDER (ID, ProviderName)
        VALUES (4, "bitStop Kohvik OÜ");''')

        #Adds records to canteen table as tuples
        table = conn.cursor()
        querry = "INSERT INTO CANTEEN (ID, ProviderID, Name, Location, time_open, time_closed) VALUES (?, ?, ?, ?, ?, ?)"
        canteenes = [
        (1, 1, 'Economics- and social science building canteen', 'Akadeemia tee 3 SOC- building', 830, 1830),
        (2, 1, 'Library canteen', 'Akadeemia tee 1/Ehitajate tee 7', 830, 1900),
        (3, 2, 'Main building Deli cafe', 'Ehitajate tee 5 U01 building', 900, 1630),
        (4, 2, 'Main building Daily lunch restaurant', 'Ehitajate tee 5 U01 building ', 900, 1630 ),
        (5, 1, 'U06 building canteen', 'U06 building canteen', 900, 1600 ),
        (6, 2, 'Natural Science building canteen','Akadeemia tee 15 SCI building', 900, 1600),
        (7, 2, 'ICT building canteen', 'Raja 15/Mäepealse 1', 900, 1600),
        (8, 3, 'Sports building canteen', 'Männiliiva 7 S01 building ', 1100, 2000)
        ]
        #Add a record to canteen table
        conn.execute('''INSERT INTO CANTEEN (ID, ProviderID, Name, Location, time_open, time_closed)
                        VALUES (9, 4, 'bitStop KOHVIK', 'IT College, Raja 4c', 930, 1600);''')
        try:
            table.executemany(querry, canteenes)
        except:
            print("Something went wrong or values already exist!")
        
        #commits the changes of the tables
        conn.commit()
        print ("Records created successfully")
    except:
         print ("Records might already exist in the database!")

def selectRecords():
    """
    selects and dispayes records from the database
    """
    print("\n========Task 1========\n")
    cursor = conn.execute('''SELECT ID, ProviderID, Name, Location, time_open, time_closed 
                             FROM CANTEEN
                             WHERE time_closed BETWEEN 1615 AND 1800;''')
    
    print("Canteens open between 16:15 and 18:00:")
    for row in cursor:
       print ("ID = ", row[0])
       print ("ProviderID = ", row[1])
       print ("Name = ", row[2])
       print ("Location = ", row[3])
       print ("time_open = ", row[4])
       print ("time_closed = ", row[5], "\n")
    
    print("\n========Task 2========\n")
    cursor = conn.execute('''SELECT CANTEEN.*, PROVIDER.*
                             FROM CANTEEN, PROVIDER
                             WHERE CANTEEN.ProviderID = PROVIDER.ID AND PROVIDER.ProviderName = "Rahva Toit"; ''')
    
    for row in cursor:
        print("Name = ", row[2])
        print("ProviderName = ", row[7], "\n")

    print ("Operation done successfully")

def closeConn():
    """
    closes the connection diners.db
    """
    conn.close()
    print ("Connection closed")

if __name__ == "__main__":
    opendb()
    createTable()
    createRecords()
    selectRecords()
    closeConn()