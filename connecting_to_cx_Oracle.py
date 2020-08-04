import os
import cx_Oracle

# Set folder in which Instant Client is installed in system path
# os.environ['PATH'] = r'D:\Softwares\python\instantclient-basiclite-windows.x64-19.6.0.0.0dbru'

# Connect to hr account in Oracle Database 11g Express Edition
con = cx_Oracle.connect("hr", "hr", "localhost")
print("Connected!")
con.close()