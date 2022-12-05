import cx_Oracle
try:
    con=cx_Oracle.connect("system/Prem0305@localhost/XE")
    cur=con.cursor()  # creating a cursor object
    #prepare the query and execute
    qry="create table Employee03(eno number(3)primary key,ename varchar2(30) not null,sal number(6,2) not null)"
    cur.execute(qry)
    print("\tTable created successfully---verify!!!")
except cx_Oracle.DatabaseError as d:
    print("Problem in database",d)