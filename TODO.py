import os
import mysql.connector

from dotenv import load_dotenv
load_dotenv()
myconnection= mysql.connector.connect(
    host= os.getenv("host"), 
    user= os.getenv("user"), 
    password= os.getenv("password"),
    database= os.getenv("database_name") )
print(myconnection)
my_cursor= myconnection.cursor()
my_cursor.execute("Create Database If Not Exists todo")
my_cursor.execute("Show Databases")
for i in my_cursor:
    print(i)

crt= "Create Table IF NOT EXISTS User (id INT PRIMARY KEY AUTO_INCREMENT, Name VARCHAR(50) NOT NULL)"
my_cursor.execute(crt)
crw= "Create Table IF NOT EXISTS Work (id INT PRIMARY KEY AUTO_INCREMENT, Task VARCHAR(100), Done CHAR, user_id INT, FOREIGN KEY(user_id) REFERENCES User (id))"
my_cursor.execute(crw)
sql1= "Insert Into User(Name) VALUES (%s)"
my_val= [
    ('rachel', ), ('Phoebe', ), ('chandler', ), ('ross', ), ('joey', ), ('monica', ), ('gunther', )
]
my_cursor.executemany(sql1, my_val)
myconnection.commit()
my_cursor.execute("SELECT DISTINCT id, Name FROM User")
usertab= my_cursor.fetchall()
for dat in usertab:
    print(dat)

sql2= "Insert Into Work(Task, Done, user_id ) VALUES (%s, %s ,%s)"
my_val2= [
    ('shop', 'y', 15), ('date','y', 16 ), ('visit','n', 17), ('grocery','y', 18), ('havefun','y', 19 ), ('dishwash','n', 20 ), ('laundry','n', 21 )
]
my_cursor.executemany(sql2, my_val2)
myconnection.commit()
my_cursor.execute("SELECT * FROM Work")
userwor= my_cursor.fetchall()
for dat1 in userwor:
    print(dat1)
