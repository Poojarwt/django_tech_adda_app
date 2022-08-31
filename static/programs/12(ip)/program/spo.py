import os 
import platform 
import mysql.connector 
 
mydb=mysql.connector.connect(host="localhost",user="root",passwd="root",database="sports") 
mycursor=mydb.cursor() 
  
def RegisterClub(): 
    L=[] 
    enroll=int(input("Enter the registration number(Max 5 Digits) : ")) 
    L.append(enroll) 
    sname=input("Enter the Name of club member: ") 
    L.append(sname) 
    age=int(input("Enter Age of member : ")) 
    L.append(age) 
    city=input("Enter the City of the member : ") 
    L.append(city) 
    sportname=input("Enter the sport name : ") 
    L.append(sportname) 
    phone=input("Enter Phone number in Digits : ") 
    L.append(phone) 
    address=input("Enter Address of member : ") 
    L.append(address) 
    regfee=int(input("Enter the registration Fee : ")) 
    L.append(regfee) 
    value=L 
    sql="insert into club (enroll,sname,age,city,sport_cls,phone,address,regfee) values (%s,%s,%s,%s,%s,%s,%s,%s)" 
    mycursor.execute(sql,value) 
    mydb.commit() 
 
def ClubView(): 
    print("Select the search criteria : ") 
    print("1. Enroll") 
    print("2. Name") 
    print("3. Age") 
    print("4. City") 
    print("5. phone") 
    print("6. Address") 
    print("7. All")
    ch=int(input("Enter the choice : ")) 
    if ch==1:  
        s=int(input("Enter enroll no : ")) 
        rl=(s,) 
        sql="select * from club where enroll=%s" 
        mycursor.execute(sql,rl) 
    elif ch==2: 
        s=input("Enter Name : ") 
        rl=(s,) 
        sql="select * from club where sname=%s" 
        mycursor.execute(sql,rl) 
    elif ch==3: 
        s=int(input("Enter age : ")) 
        rl=(s,) 
        sql="select * from club where age=%s" 
        mycursor.execute(sql,rl) 
    elif ch==4: 
        s=input("Enter City : ") 
        rl=(s,) 
        sql="select * from club where City=%s" 
        mycursor.execute(sql,rl) 
    elif ch==5: 
        s=input("Enter phone : ") 
        rl=(s,) 
        sql="select * from club where phone=%s" 
        mycursor.execute(sql,rl) 
    elif ch==6: 
        s=input("Enter address : ") 
        rl=(s,) 
        sql="select * from club where address=%s" 
        mycursor.execute(sql,rl) 
    elif ch==7: 
        sql="select * from club" 
        mycursor.execute(sql) 
    res=mycursor.fetchall() 
    print("The Memebers details are as follows : ") 
    print("(ROll, Name, Age, Class, City)") 
    for x in res: 
        print(x) 
 
def UpdateClub():
     tempst=int(input("Enter Enrollment No : "))
     print("1.Name\n2.Age\n3.City\n4.Class\n5.Phone no.\n6.Address\n7.Registration\n8.Exit Fee")
     opt=int(input("Select the option you want to update: "))
     if opt==1:
         temp=input("Enter the new name: ")
         try:
            sql = "Update club set sname='%s' where enroll=%s" % (temp,tempst) 
            mycursor.execute(sql) 
            mydb.commit() 
         except Exception as e: 
            print (e)
            mydb.close()
     elif opt==2:
         temp=input("Enter the new Age: ")
         try: 
            sql = "Update club set Age=%s where enroll=%s" % (temp,tempst) 
            mycursor.execute(sql) 
            mydb.commit() 
         except Exception as e: 
            print (e)
            mydb.close()
     elif opt==3:
         temp=input("Enter the new City: ")
         try: 
            sql = "Update club set city='%s' where enroll=%s" % (temp,tempst) 
            mycursor.execute(sql) 
            mydb.commit() 
         except Exception as e: 
            print (e)
            mydb.close()
     elif opt==4:
         temp=input("Enter the new sports class: ")
         try: 
            sql = "Update club set sport_cls='%s' where enroll=%s" % (temp,tempst) 
            mycursor.execute(sql) 
            mydb.commit() 
         except Exception as e: 
            print (e)
            mydb.close()
     elif opt==5:
         temp=input("Enter the new Phone number: ")
         try: 
            sql = "Update club set phone='%s' where enroll=%s" % (temp,tempst) 
            mycursor.execute(sql) 
            mydb.commit() 
         except Exception as e: 
            print (e)
            mydb.close()
     elif opt==6:
         temp=input("Enter the new Address: ")
         try: 
            sql = "Update club set address='%s' where enroll=%s" % (temp,tempst) 
            mycursor.execute(sql) 
            mydb.commit() 
         except Exception as e: 
            print (e)
            mydb.close()
     elif opt==7:
         temp=input("Enter the new Registration Fees: ")
         try: 
            sql = "Update club set regfee=%s where enroll=%s" % (temp,tempst) 
            mycursor.execute(sql) 
            mydb.commit() 
         except Exception as e: 
            print (e)
            mydb.close()
     elif opt==8:
         Menuset()
     else:
        print("Enter a correct option:")
        updateclub()

def RemoveClub(): 
    enroll=int(input("Enter the enroll number of the memeber to be deleted : ")) 
    rl=(enroll,) 
    sql="Delete from club where enroll=%s" 
    mycursor.execute(sql,rl) 
    mydb.commit() 
 
 
def MenuSet(): 
    print("\n")
    print("******************WELCOME TO SPORTS CLUB**********************")
    print("------------------------------------------")
    print("Enter 1 : To Register Club") 
    print("Enter 2 : To View Club ") 
    print("Enter 3 : To Update Club ") 
    print("Enter 4 : To Remove Club") 
    print("------------------------------------------")
    userInput = int(input("Please Select An Above Option: ")) 
    print("\n")  
    if(userInput == 1): 
        RegisterClub()
        MenuSet()
    elif (userInput==2): 
        ClubView()
        MenuSet()
    elif (userInput==3): 
        UpdateClub()
        MenuSet()
    elif (userInput==4): 
        RemoveClub()
        MenuSet()
    else: 
        print("Enter correct choice. . . ") 

MenuSet() 
 
