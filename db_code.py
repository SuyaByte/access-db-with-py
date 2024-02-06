import sqlite3
import pandas as pd 

conn = sqlite3.connect('STAFF.db')

tablename = 'INSTRUCTOR'

attributes = ['ID','FNAME','LNAME','CITY','CCODE']

filepath = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(filepath,names = attributes)

df.to_sql(tablename,conn,if_exists = 'replace',index = False)
print("Table is ready")

query1 = f"SELECT * from {tablename}"
qout = pd.read_sql(query1,conn)
print(query1)
print(qout)

query1 = f"SELECT FNAME from {tablename}"
qout = pd.read_sql(query1,conn)
print(query1)
print(qout)

query1 = f"SELECT count(*) from {tablename}"
qout = pd.read_sql(query1,conn)
print(query1)
print(qout)

data_dict = {'ID':[100],'FNAME':['John'],'LNAME':['Doe'],'CITY':'Paris','CCODE':'FR'}
data_append = pd.DataFrame(data_dict)

data_append.to_sql(tablename,con=conn,if_exists = 'append',index=False)
print("Data appended successfully")

query1=f"SELECT COUNT(*) FROM {tablename}"
qout = pd.read_sql(query1,conn)
print(query1)
print(qout)

conn.close()