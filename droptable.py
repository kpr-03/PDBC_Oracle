#this program will remove the table from oracle DB.
import cx_Oracle
try:
    con=cx_Oracle.connect("system/Prem0305@localhost/XE")
    cur=con.cursor()
    cur.execute("drop table student")
    print("Table dropped succesfully")
except cx_Oracle.Databaserror as db:
    print("Problem in Database",db) 