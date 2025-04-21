import sqlite3
conn = sqlite3.connect('database.sqlite')
cursor = conn.cursor()
print("Opened database successfully")

cursor.execute('''CREATE TABLE EMPLOYEE
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         AGE            INT     NOT NULL);''')


cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE) VALUES (1, 'Razi', 14)")
cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE) VALUES (2, 'Jon', 19)")
cursor.execute("INSERT INTO EMPLOYEE (ID,NAME,AGE) VALUES (3, 'Martha', 35)")
# conn.execute("DELETE from EMPLOYEE where ID = 2")
conn.commit()



cursor.execute("SELECT * FROM EMPLOYEE")
rows = cursor.fetchall()
for row in rows:
    print(row)

cursor.close()
conn.close()
