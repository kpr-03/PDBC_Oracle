#program for obtaining connection from oracle-DB
import cx_Oracle
try:
    con=cx_Oracle.connect("system/Prem0305@localhost/XE")
    print("Python program obtains connection from Oracle DB")
    print("Type of con=",type(con))
except cx_Oracle.DatabaseError as db:
    print("Problem in oracle",db)