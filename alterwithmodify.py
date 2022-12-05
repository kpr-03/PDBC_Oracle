import cx_Oracle
def tablemodify():
    try:
        con=cx_Oracle.connet("system/Prem0305@localhost/XE")
        #prepare the query and execute.
        cur=con.cursor()
        qry="alter table employee modify(eno number(4),sal number(7,2))"
        cur.execute(qry)
        print("\tTable altered successfully---verify!!!")
    except cx_Oracle.DatabaseError as d:
        print("problem in database",d)
#main program
tablemodify()