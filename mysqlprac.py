import mysql.connector as mysql
from tabulate import tabulate

connection = mysql.connect(host='localhost', user='root')
print("Connection successfully")
cursor = connection.cursor()

# Creating Database
print("List of all Database present in server:")
cursor.execute('create database maha;')
cursor.execute('show databases;')
print(tabulate(cursor.fetchall(), headers=('Databases',), tablefmt='psql', numalign='left'))

# Using Database
cursor.execute('use maha')
print("Database Changed -> maha", end='\n'*2)

# Creating Table
print("Table Created in Database")
cursor.execute('create table students (name varchar(20), rollno int(3))')
cursor.execute('show tables;')
print(tabulate(cursor.fetchall(), headers=('Tables in Database',), tablefmt='psql', numalign='left'))

# Inserting Values (Single)
print("Inserting Values (Single)")
query = 'INSERT INTO students VALUES ("Zaeem", "425")'
cursor.execute(query)
cursor.execute('select * from students;')
print(tabulate(cursor.fetchall(), headers=('Name', 'Roll no'), tablefmt='psql', numalign='left'))

#INSERTING VALUES (MULTI)
print("Inserting Values (Multi)")
query = 'INSERT INTO students VALUES (%s, %s)'
data = [("safdar", '424'), ('doja', '417')]
cursor.executemany(query, data)
cursor.execute('select * from students;')
print(tabulate(cursor.fetchall(), headers=('Name', 'Roll no'), tablefmt='psql', numalign='left'))

#UPDATING VAlUES
print('Updating Values in Table')
cursor.execute('UPDATE students set name="raza", rollno="444" where name="Zaeem"')
cursor.execute('select * from students;')
print(tabulate(cursor.fetchall(), headers=('Name', 'Roll no'), tablefmt='psql', numalign='left'))

#DELETING Values
print('Deleting Values from Table')
cursor.execute('DELETE from students where name="doja"')
cursor.execute('select * from students;')
print(tabulate(cursor.fetchall(), headers=('Name', 'Roll no'), tablefmt='psql', numalign='left'))

connection.commit()  # commiting changes to mysql server
cursor.close()      # closing cursor
connection.close()  # closing connection

print('Coded By Durani Mohammed Zaeem, Roll no: 425')