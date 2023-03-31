import sqlite3

conn= sqlite3.connect('test.db')
print("opened successfully")

commmand="create table todo (id int, task text, date text, status text)"
conn.execute(command)
print("table created")