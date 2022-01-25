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

#Создание таблицы:
#cur.execute('''CREATE TABLE STUDENT (ADMISSION INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL, COURSE CHAR(50), DEPARTMENT CHAR(50));''')
#con.commit()
#print("Table created successfully")

#Вставка запись в таблицу STUDENT:
#cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3420, 'John', 18, 'Computer Science', 'ICT')")
#con.commit()
#print("Record inserted successfully") 


#Вставить несколько записей в таблицу STUDENT:
#cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3419, 'Abel', 17, 'Computer Science', 'ICT')")  
#cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3421, 'Joel', 17, 'Computer Science', 'ICT')")  
#cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3422, 'Antony', 19, 'Electrical Engineering', 'Engineering')")  
#cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (3423, 'Alice', 18, 'Information Technology', 'ICT')")
#con.commit()
#print("Records inserted successfully") 

#Извлечение данных:
#cur.execute("SELECT admission, name, age, course, department from STUDENT")
#rows = cur.fetchall()
#for row in rows:  
#   print("ADMISSION =", row[0])
#   print("NAME =", row[1])
#   print("AGE =", row[2])
#   print("COURSE =", row[3])
#   print("DEPARTMENT =", row[4], "\n")
#con.commit()
#print("Operation done successfully")  


#Обновить значение в таблице и просмотреть:
#cur.execute("UPDATE STUDENT set AGE = 20 where ADMISSION = 3420")  
#con.commit()  
#print("Total updated rows:", cur.rowcount)

#cur.execute("SELECT admission, age, name, course, department from STUDENT")  
#rows = cur.fetchall()  
#for row in rows:  
#   print("ADMISSION =", row[0])
#   print("NAME =", row[1])
#   print("AGE =", row[2])
#   print("COURSE =", row[2])
#   print("DEPARTMENT =", row[3], "\n")
#print("Operation done successfully")  

#Удалить строку в таблице и просмотреть:
#cur.execute("DELETE from STUDENT where ADMISSION=3420;")  
#con.commit()  

#print("Total deleted rows:", cur.rowcount)
#cur.execute("SELECT admission, name, age, course, department from STUDENT")  
#rows = cur.fetchall()  
#for row in rows:  
#   print("ADMISSION =", row[0])
#   print("NAME =", row[1])
#   print("AGE =", row[2])
#   print("COURSE =", row[3])
#   print("DEPARTMENT =", row[4], "\n")

#print("Deletion successful")  


con.close()
