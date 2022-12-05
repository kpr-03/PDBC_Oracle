#progam for inserting the recrds in employee table
import cx_Oracle,sys
def empinsert():
    while(True):
        try:
            con=cx_Oracle.connect("system/Prem0305@localhost/XE")
            cur=con.cursor()
            print("-"*50)
            #accept the employee details from KBD
            empno=int(input("Enter Employee number:"))
            ename=input("Enter Employee Name:")
            sal=float(input("Enter Employee salary:"))
            cname=input("Enter Employee Company Name:")
            #prepare the query and execute
            iq="insert into employee values(%d,'%s',%f,'%s')"
            con.commit()
            print("-"*50)
            print("Employee record inserted successfuly!".format(cur.rowcount))
            print("-"*50)
            ch=input("Do you want to insert another record(yes/no):")
            if(ch.lower()=="no"):
                print("thanx for usingh this program")
                sys.exit()
        except cx_Oracle.DatabaseError as db:
            print("Problem in database",db)
        except ValueError:
            print("Don't enter strs/symbols/alnums for eno and sals")
            
#main program
empinsert()