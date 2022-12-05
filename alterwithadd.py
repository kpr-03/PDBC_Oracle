import cx_Oracle
def tablemodify():
    try:
        con=cx_Oracle.connect("system/Prem0305@localhost/XE")
        cur=con.cursor()
        #prepare the query and execute.
        qry="alter table employee add(cname varchar2(10))"
        cur.execute(qry)
        print("\tTable altered successfully---verify")
    except cx_Oracle.DatabaseError as d:
        print("problem in Database",d)
#main program
tablemodify()