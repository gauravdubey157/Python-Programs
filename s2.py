import sqlite3
conn=sqlite3.connnect('test.db')
print("opened successfully")

command="insert into todo(id, task, date, status) values(1,'study ml','23/12/22','not done')"
conn.execute(command)