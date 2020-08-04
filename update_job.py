import sqlite3

con = sqlite3.connect(r"d:\Programs_OnlineClasses\CorePython_14_07\hr.db")
cur=con.cursor()

try:
    id = int(input("Enter the Id : "))
    minsalary = int(input("Enter the minsalary : "))

    cur.execute("update job set minsalary=? where id =? ",(minsalary,id))

    if cur.rowcount==1:
        print("Updated Job table Succesfully!")
        con.commit()
    else:
        print("Job ID not found!")
except Exception as ex:
    print("Error",ex)
con.close()

