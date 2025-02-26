import sqlite3
conn = sqlite3.connect("data.db")
print("opened database successfully")
conn.execute("CREATE TABLE sai(username varchar,email varchar,password varchar)")
print("table created successfully")
conn.close()