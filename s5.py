import sqlite3
conn=sqlite3.connect('test.db')
print("opened successfully")

command="delete from todo where id=1"
conn.execute(command)
conn.commit()

print("total changes". conn.total_changes)

result=conn.execute("select * from todo")