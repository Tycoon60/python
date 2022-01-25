#!/usr/bin/env python3

import psycopg2

con = psycopg2.connect(
  database="database1", 
  user="dmosk", 
  password="myPassword", 
  host="192.168.242.205", 
  port="5432"
)

print("Database opened successfully")

cur = con.cursor()  
cur.execute('''CREATE TABLE STUDENT  
     (ADMISSION INT PRIMARY KEY NOT NULL,
     NAME TEXT NOT NULL,
     AGE INT NOT NULL,
     COURSE CHAR(50),
     DEPARTMENT CHAR(50));''')

print("Table created successfully")
con.commit()  
con.close()
