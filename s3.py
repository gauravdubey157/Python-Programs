import sqlite3
conn=sqlite3.connect('test.db')
print("opened successfully")

command="select * from todo"
result=conn.execute(command)
r=result.fetchall()
print(r)