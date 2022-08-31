import mysql.connector as sqlcon
#connecting to database
mycon = sqlcon.connect(host='localhost',user='root',password='root',database='student_data')
if mycon.is_connected==False:
    print("Error connecting to mysql database")
cursor=mycon.cursor()
#giving sql query
cursor.execute("select * from stu_info")
#retrieve all the data from table stu_info from sql database student_data
data=cursor.fetchall()
for row in data:
    print(row)
