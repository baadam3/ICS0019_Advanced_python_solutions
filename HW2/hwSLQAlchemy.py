import sqlalchemy
from sqlalchemy.orm import sessionmaker

'''
This is the solution for homework 2 using SQLAlchemy
'''



def connectDB():
   '''
    Opens connection to the database, or creates it if it's missing
   '''
   global database
   database = sqlalchemy.create_engine('sqlite:///C:\\Users\\adamb\Desktop\\Advanced Python\\dinersA.db', echo = False)
   global conn
   conn = database.connect()
   global meta
   meta = sqlalchemy.MetaData()
   print("Database opened successfully!")

def createTable():
    '''
    Creates tables in database with SQLAlchemy
    '''
    global PROVIDER
    PROVIDER = sqlalchemy.Table(
        'PROVIDER', meta,
        sqlalchemy.Column('ID', sqlalchemy.Integer, primary_key = True, nullable = False),
        sqlalchemy.Column('ProviderName', sqlalchemy.String, nullable = False),
    )

    global CANTEEN
    CANTEEN = sqlalchemy.Table(
        'CANTEEN', meta,
        sqlalchemy.Column('ID', sqlalchemy.Integer, primary_key = True, nullable = False),
        sqlalchemy.Column('ProviderID',sqlalchemy.Integer, nullable = False),
        sqlalchemy.Column('Name', sqlalchemy.String, nullable = False),
        sqlalchemy.Column('Location', sqlalchemy.String),
        sqlalchemy.Column('time_open',sqlalchemy.Integer),
        sqlalchemy.Column('time_closed',sqlalchemy.Integer),
        sqlalchemy.ForeignKeyConstraint(['ProviderID'],['PROVIDER.ID'])
    )

    meta.create_all(database)
    print("Tables created!")

def insertData():
    '''
    Adds data to database with SQLAlchemy
    '''

    p1 = (sqlalchemy.insert(PROVIDER).
            values(ID = 1, ProviderName = 'Rahva Toit'))
    p2 = (sqlalchemy.insert(PROVIDER).
            values(ID = 2, ProviderName = 'Baltic Restaurants Estonia AS'))
    p3 = (sqlalchemy.insert(PROVIDER).
            values(ID = 3, ProviderName = 'TTÜ Sport OÜ'))
    p4 = (sqlalchemy.insert(PROVIDER).
            values(ID = 4, ProviderName = 'bitStop Kohvik OÜ'))

    try:
        conn.execute(p1)
        conn.execute(p2)
        conn.execute(p3)
        conn.execute(p4)
        conn.execute(CANTEEN.insert(), [
            {"ID":1,'ProviderID':1,'Name':'Economics- and social science building canteen','Location':'Akadeemia tee 3 SOC- building','time_open':830,'time_closed':1830},
            {"ID":2,'ProviderID':1,'Name':'Library canteen','Location':'Akadeemia tee 1/Ehitajate tee 7','time_open':830,'time_closed':1900},
            {"ID":3,'ProviderID':2,'Name':'Main building Deli cafe','Location':'Ehitajate tee 5 U01 building','time_open':900,'time_closed':1630},
            {"ID":4,'ProviderID':2,'Name':'Main building Daily lunch restaurant','Location':'Ehitajate tee 5 U01 building','time_open':900,'time_closed':1630},
            {"ID":5,'ProviderID':1,'Name':'U06 building canteen','Location':'U06 building canteen','time_open':900,'time_closed':1600},
            {"ID":6,'ProviderID':2,'Name':'Natural Science building canteen','Location':'Akadeemia tee 15 SCI building','time_open':900,'time_closed':1600},
            {"ID":7,'ProviderID':2,'Name':'ICT building canteen','Location':'Raja 15/Mäepealse 1','time_open':900,'time_closed':1600},
            {"ID":8,'ProviderID':3,'Name':'Sports building canteen','Location':'Männiliiva 7 S01 building','time_open':1100,'time_closed':2000},
        ])
        conn.execute(CANTEEN.insert(),{"ID":9,'ProviderID':4,'Name':'bitStop KOHVIK','Location':'IT College, Raja 4c','time_open':930,'time_closed':1600})
        print("Data added successfully!")
    except:
        print("Something went wrong or data already exists!")

def selectRecords():
    '''
    Makes queries with SQLAlchemy
    '''
    canteen = CANTEEN.select().where(CANTEEN.c.time_closed.between(1615, 1800))
    query = conn.execute(canteen)

    print("\n========Task 1 ========\n")
    for row in query:
       print ("ID = ", row[0])
       print ("ProviderID = ", row[1])
       print ("Name = ", row[2])
       print ("Location = ", row[3])
       print ("time_open = ", row[4])
       print ("time_closed = ", row[5], "\n")

    provID = conn.execute('''SELECT CANTEEN.*, PROVIDER.*
                             FROM CANTEEN, PROVIDER
                             WHERE CANTEEN.ProviderID = PROVIDER.ID AND PROVIDER.ProviderName = "Rahva Toit";''')
    print("\n========Task 2 ========\n")
    for row in provID:
        print("Name = ", row[2])
        print("ProviderName = ", row[7], "\n")


def connClose():
    #Closes the connection to the database
    conn.close()  

if __name__ == "__main__":
    connectDB()
    createTable()
    insertData()
    selectRecords()
    connClose()