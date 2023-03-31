import sqlite3
conn=sqlite3.connect('test.db')
print("opened successfully")

command="update todo set status='done' where id=2"
conn.execute(command)
conn.commit()

print("total changes", conn.total_changes)
result = conn.execute("select * from todo")
for row in result:
    print(row)
 