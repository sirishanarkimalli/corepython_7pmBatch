import sqlite3
import json

con = sqlite3.connect(r"d:\Programs_OnlineClasses\CorePython_14_07\hr.db")
cur=con.cursor()
cur.execute("select * from job")

jobs=[]
for row in cur.fetchall():
    jobs.append({'id':row[0],'title':row[1],'minsalary':row[2]})

f= open("job.json","wt")
json.dump(jobs,f)

f.close()
con.close()