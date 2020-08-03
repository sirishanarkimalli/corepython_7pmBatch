import sqlite3

con = sqlite3.connect(r"d:\Programs_OnlineClasses\CorePython_14_07\hr.db")
cur=con.cursor()
cur.execute("select * from job")

for row in cur.fetchall():
    print(f"{row[1]:25}  {row[2]:10}")

con.close()
