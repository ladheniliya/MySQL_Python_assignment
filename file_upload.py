import pandas as pd
import glob
import os

arr = os.listdir('F:\project\mysql_project\mysql_py\csv-files')
print(arr)

path = r'F:\project\mysql_project\mysql_py\csv-files' # use your path
all_files = glob.glob(path + "/*.csv")

file_inserted = ['F:\\project\\mysql_project\\mysql_py\\csv-files\\1.csv']

file_count=0
data_all = []

for filename in all_files:
    if file_inserted.__contains__(filename):
        pass
    else:
        df = pd.read_csv(filename, index_col=None, header=0)
        data_all.append(df)
        file_count += 1
print(data_all)
print("file_count: "+str(file_count))
print("append successful")
frame = pd.concat(data_all, axis=0, ignore_index=True,sort=True)
print(frame)
df = pd.DataFrame(frame)
df.to_csv('F:\\project\\mysql_project\\mysql_py\\filename.csv', header=True, index=False)
print(df)

#################################################################################

####connection to mysql#################33
import mysql.connector
import csv
from csv import reader

import pymysql.cursors
import pymysql.connections
connection = pymysql.connect(host='localhost',
                                              user='root',
                                              password='root',
                                              database='mysql',
                                              charset='utf8mb4',
                                              cursorclass=pymysql.cursors.DictCursor)
#getDBConnection()
cur = connection.cursor()
cur = connection.cur()
#cursor.execute("DROP database IF EXISTS MyDatabase")
#sql = "CREATE database MYDATABASE";
cur.execute("SELECT DATABASE()")
#cursor.execute(sql)
data = cur.fetchone()
print("Connection established to: ",data)
print("List of databases: ")
cur.execute("SHOW DATABASES")
print(cur.fetchall())

use_db = "use mysql"
cur.execute(use_db)

sql1 ="CREATE TABLE fun(id int ,fname VARCHAR(20) NOT NULL,lname VARCHAR(20))"
cur.execute(sql1)

desc = "describe fun"
cur.execute(desc)

#######INSERT#########3

df = pd.read_csv('F:\\project\\mysql_project\\mysql_py\\filename.csv')
columns = ['id','fname','lname']
df_data = df[columns]
records = df_data.values.tolist()
#print(records)
for i in records:
#    print(i)
 #   print("INSERT INTO fun('id','fname','lname') VALUES (%s,%s,%s)",(i[0],i[1],i[2]))
    cur.execute("INSERT INTO fun(id,fname,lname) VALUES (%s,%s,%s)", (i[0],i[1],i[2]))
    connection.commit()
    
#try:
#    cur = connection.cur()
#    cursor.executemany(sql_insert, records)
#    cursor.commit()  
#except:
#    pass
#finally:
#    print('Task is complete.')
#    

s = "select * from fun"
cur.execute(s)
print(cur.fetchall())


cur.close()

connection.close()
