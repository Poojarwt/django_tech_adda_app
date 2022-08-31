import os 
import platform 
import mysql.connector  

def selection(): 
 db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
 cursor = db.cursor() 
 print('-----------------------------------\nWELCOME TO SCHOOL MANAGEMENT SYSTEM\n-----------------------------------')
 print('***************************')
 print("1.STUDENT MANAGEMENT") 
 print("2.EMPLOYEE MANAGEMENT") 
 print("3.FEE MANAGEMENT") 
 print("4.EXAM MANAGEMENT")
 print('***************************')
 
 ch=int(input("\nEnter ur choice (1-4): ")) 
 if ch==1: 
     stu_management()
 elif ch==2: 
     emp_management()
 elif ch==3: 
     fee_management()
 elif ch==4: 
     exam_management()
 else: 
     print('Enter correct choice..!!')
     selection()
     
def stu_management():
     print('******************************************')
     print('\nWELCOME TO STUDENT MANAGEMENT SYSTEM\n')
     print('a.VIEW STUDENTS DETAILS')
     print('b.NEW ADMISSION') 
     print('c.UPDATE STUDENT DETAILS') 
     print('d.ISSUE TC')
     print('e.EXIT')
     print('******************************************')
     c=input("Enter ur choice (a-e):") 
     if c=='a':
         print('\nStudents details are as follows..\n') 
         display1()
         stu_management()
     elif c=='b':
         insert1() 
         print('\nModified details are..\n') 
         display1()
         stu_management()
     elif c=='c':
         update1() 
         print('\nModified details are..\n')
         display1()
         stu_management()
     elif c=='d':
         delete1() 
         print('\nModified details are..\n') 
         display1()
         stu_management()
     elif c=='e': 
          selection()
     else: 
         print('Enter correct choice...!!')
         stu_management()
         
def emp_management():
     print('******************************************')
     print('WELCOME TO EMPLOYEE MANAGEMENT SYSTEM')
     print('a.VIEW EMPLOYEE DETAILS')
     print('b.NEW EMPLOYEE') 
     print('c.UPDATE STAFF DETAILS') 
     print('d.DELETE EMPLOYEE')
     print('e.EXIT')
     print('******************************************')
     c=input("Enter ur choice (a-e):")
     if c=='a':
         print('Employee details are as follows:')
         display2()
         emp_management()
     elif c=='b': 
         insert2()
         print('\nModified details are..\n') 
         display2()
         emp_management()
     elif c=='c': 
         update2() 
         print('\nModified details are..\n') 
         display2()
         emp_management()
     elif c=='d': 
         delete2() 
         print('\nModified details are..\n') 
         display2()
         emp_management()
     elif c=='e':
          selection()
     else: 
         print('Enter correct choice...!!')
         emp_management()

def fee_management():
     print('******************************************')
     print('WELCOME TO FEE MANAGEMENT SYSTEM') 
     print('a.NEW FEE') 
     print('b.UPDATE FEE') 
     print('c.EXEMPT FEE')
     print('d.EXIT')
     print('******************************************')
     c=input("Enter ur choice (a-d):")
     if c=='a': 
         insert3()
         print('\nModified details are..\n')
         display3()
         fee_management()
     elif c=='b': 
         update3()
         print('\nModified details are..\n')
         display3()
         fee_management()
     elif c=='c': 
         delete3()
         print('\nModified details are..\n')
         display3()
         fee_management()
     elif c=='d': 
          selection()
     else: 
         print('Enter correct choice...!!')
         fee_management()

def exam_management():
     print('******************************************')
     print('WELCOME TO EXAM MANAGEMENT SYSTEM') 
     print('a.EXAM DETAILS') 
     print('b.UPDATE DETAILS ') 
     print('c.DELETE DETAILS')
     print('d.EXIT')
     print('******************************************')
     c=input("Enter ur choice (a-d):")
     if c=='a': 
         insert4()
         print('\nModified details are..\n')
         display4()
         exam_management()
     elif c=='b': 
         update4()
         print('\nModified details are..\n')
         display4()
         exam_management()
     elif c=='c': 
         delete4()
         print('\nModified details are..\n')
         display4()
         exam_management()
     elif c=='d': 
          selection()
     else: 
         print('Enter correct choice...!!')
         exam_management()
           
      
def insert1(): 
    sname=input("Enter Student Name : ") 
    admno=int(input("Enter Admission No : ")) 
    dob=input("Enter Date of Birth(yyyy-mm-dd): ") 
    cls=input("Enter class for admission: ") 
    cty=input("Enter City : ") 
    db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
    cursor = db.cursor()
    sql="INSERT INTO student(sname,admno,dob,cls,cty) VALUES ( '%s' ,'%d','%s','%s','%s')"%(sname,admno,dob,cls,cty) 
    try: 
       cursor.execute(sql) 
       db.commit() 
    except: 
        db.rollback() 
        db.close()
         
def display1(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM student"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
        for c in results: 
            sname = c[0] 
            admno= c[1] 
            dob=c[2] 
            cls=c[3] 
            cty=c[4] 
            print ("(sname=%s,admno=%d,dob=%s,cls=%s,cty=%s)" % (sname,admno,dob,cls,cty)) 
    except: 
        print ("Error: unable to fetch data") 
        db.close() 
def update1(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM student"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
 
        for c in results: 
            sname = c[0] 
            admno= c[1] 
            dob=c[2] 
            cls=c[3] 
            cty=c[4]        
    except: 
        print ("Error: unable to fetch data") 
    print() 
    tempst=int(input("Enter Admission No : "))     
    temp=input("Enter new class  : ") 
    try: 
        sql = "Update student set cls=%s where admno='%d'" % (temp,tempst) 
        cursor.execute(sql) 
        db.commit() 
    except Exception as e: 
        print (e)
        db.close() 
def delete1(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM student"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
        for c in results: 
            sname = c[0] 
            admno= c[1] 
            dob=c[2] 
            cls=c[3] 
            cty=c[4] 
    except: 
        print ("Error: unable to fetch data") 
 
    temp=int(input("\nEnter adm no to be deleted : ")) 
    try: 
        sql = "delete from student where admno='%d'" % (temp) 
        ans=input("Are you sure you want to delete the record(y/n) : ") 
        if ans=='y' or ans=='Y': 
            cursor.execute(sql) 
            db.commit() 
    except Exception as e: 
        print (e) 
        db.close()
        
def insert2(): 
    ename=input("Enter Employee Name : ") 
    empno=int(input("Enter Employee No : ")) 
    job=input("Enter Designation: ") 
    hiredate=input("Enter date of joining: ") 
    db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
    cursor = db.cursor() 
    sql="INSERT INTO emp(ename,empno,job,hiredate) VALUES ( '%s' ,'%d','%s','%s')"%(ename,empno,job,hiredate) 
    try: 
       cursor.execute(sql) 
       db.commit() 
    except: 
        db.rollback() 
        db.close()
        
def display2(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM emp"  
        cursor.execute(sql) 
        results = cursor.fetchall()
        for c in results: 
           empno= c[0]
           ename = c[1] 
           job = c[2] 
           hiredate=c[3]   
           print ("(empno=%d,ename=%s,job=%s,hiredate=%s)" % (empno,ename,job,hiredate))
    except: 
        print ("Error: unable to fetch data") 
        db.close() 
def update2(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM emp"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
        for c in results: 
            empno= c[0]
            ename = c[1] 
            job=c[2] 
            hiredate=c[3]
    except: 
        print ("Error: unable to fetch data") 
    print() 
    tempst=int(input("Enter Employee No : "))     
    temp=input("Enter new designation  : ") 
    try: 
        sql = "Update emp set job='%s' where empno='%d'" % (temp,tempst) 
        cursor.execute(sql) 
        db.commit() 
    except Exception as e: 
        print (e)
        db.close() 

def delete2(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM emp"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
        for c in results: 
            empno= c[0]
            ename = c[1] 
            job=c[2] 
            hiredate=c[3]   
    except: 
        print ("Error: unable to fetch data") 
 
    temp=int(input("\nEnter emp no to be deleted : ")) 
    try: 
        sql = "delete from emp where empno='%d'" % (temp) 
        ans=input("Are you sure you want to delete the record(y/n) : ") 
        if ans=='y' or ans=='Y': 
            cursor.execute(sql)
            db.commit() 
    except Exception as e: 
        print (e) 
        db.close() 
def insert3(): 
    admno=int(input("Enter adm no: ")) 
    fee=float(input("Enter fee amount : ")) 
    month=input("Enter Month: ")
    status=input("Enter Status: ")
    db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
    cursor = db.cursor() 
    sql="INSERT INTO fee(admno,fee,month,status) VALUES ( '%d','%d','%s','%s')"%(admno,fee,month,status) 
    try: 
       cursor.execute(sql) 
       db.commit() 
    except: 
        db.rollback() 
        db.close() 
def display3(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM fee"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
        for c in results: 
            admno= c[0] 
            fee=c[1] 
            month=c[2]
            status=c[3]
            print ("(admno=%d,fee=%s,month=%s,status=%s)" % (admno,fee,month,status)) 
    except: 
        print ("Error: unable to fetch data") 
        db.close() 
def update3(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM fee"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
        for c in results: 
            admno= c[0] 
            fee=c[1] 
            month=c[2]
            status=c[3]
    except: 
        print ("Error: unable to fetch data") 
    print() 
    tempst=int(input("Enter Admission No : "))     
    temp=input("Enter new Status  : ") 
    try: 
        sql = "Update fee set status='%s' where admno='%d'" % (temp,tempst) 
        cursor.execute(sql)
        db.commit() 
    except Exception as e: 
        print (e) 
        db.close() 
def delete3(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM fee"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
        for c in results: 
            admno= c[0] 
            fee=c[1] 
            month=c[2]
            status=c[3]
    except: 
        print ("Error: unable to fetch data") 
 
    temp =int(input("\nEnter adm no to be deleted : ")) 
    try: 
        sql = "delete from fee where admno='%d'" % (temp) 
        ans=input("Are you sure you want to delete the record(y/n) : ") 
        if ans=='y' or ans=='Y': 
            cursor.execute(sql) 
            db.commit() 
    except Exception as e: 
        print (e) 
        db.close() 
def insert4(): 
    sname=input("Enter Student Name : ") 
    admno=int(input("Enter Admission No : ")) 
    per=float(input("Enter percentage : ")) 
    res=input("Enter result: ") 
    db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
    cursor = db.cursor() 
    sql="INSERT INTO exam(sname,admno,per,res) VALUES ( '%s' ,'%d','%s','%s')"%(sname,admno,per,res)  
    try: 
       cursor.execute(sql) 
       db.commit() 
    except: 
        db.rollback() 
        db.close() 
def display4(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM exam"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
        for c in results: 
            sname = c[0]
            admno= c[1] 
            per=c[2] 
            res=c[3] 
            print ("(sname=%s,admno=%d,per=%d,res=%s)"%(sname,admno,per,res)) 
    except: 
        print ("Error: unable to fetch data") 
        db.close() 
 
def update4(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM exam"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
        for c in results: 
            sname = c[0] 
            admno= c[1] 
            per=c[2] 
            res=c[3]         
    except: 
        print ("Error: unable to fetch data") 
    print() 
    tempst=int(input("Enter Admission No : "))     
    temp=input("Enter new result  : ") 
    try: 
        sql = "Update exam set res='%s' where admno='%d'" % (temp,tempst) 
        cursor.execute(sql) 
        db.commit() 
    except Exception as e: 
        print (e) 
        db.close() 
def delete4(): 
    try: 
        db = mysql.connector.connect(user='root', password='root', host='localhost',database='student_management') 
        cursor = db.cursor() 
        sql = "SELECT * FROM exam"  
        cursor.execute(sql) 
        results = cursor.fetchall() 
        for c in results: 
            sname = c[0] 
            admno= c[1] 
            per=c[2] 
            res=c[3] 
    except: 
        print ("Error: unable to fetch data")
        
    temp=int(input("\nEnter adm no to be deleted : ")) 
    try: 
        sql = "delete from exam where admno='%d'" % (temp) 
        ans=input("Are you sure you want to delete the record(y/n) : ") 
        if ans=='y' or ans=='Y': 
            cursor.execute(sql) 
            db.commit() 
    except Exception as e: 
        print (e) 
        db.close() 
selection() 
