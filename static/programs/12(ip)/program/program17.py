import mysql.connector as sqlcon
#connecting to database
mycon = sqlcon.connect(host='localhost',user='root',password='root',database='student_data')
if mycon.is_connected==False:
    print("Error connecting to mysql database")
cursor=mycon.cursor()
#update data into the database
data="update stu_info set stu_marks={} where stu_marks={}".format(79,77)
cursor.execute(data)
mycon.commit()
#retrieve all the updated data from table stu_info from sql database student_data
cursor.execute("select * from stu_info")
show=cursor.fetchall()
for row in show:
    print(row)
