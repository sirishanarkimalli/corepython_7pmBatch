import sqlite3

con = sqlite3.connect(r"d:\Programs_OnlineClasses\CorePython_14_07\hr.db")
cur=con.cursor()

try:
    title = input("Enter the title : ")
    minsalary = int(input("Enter the minsalary : "))
    cur.execute("insert into job(title,minsalary) values(?,?)",(title,minsalary))
    # cur.execute("delete from job where id =?",(id,))

    if cur.rowcount == 1:
        print("Added or inserted one Job Succesfully!")
        con.commit()
except Exception as ex:
    print("Error",ex)
con.close()