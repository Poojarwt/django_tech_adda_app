import mysql.connector as sqlcon
#connecting to database
mycon = sqlcon.connect(host='localhost',user='root',password='root',database='student_data')
if mycon.is_connected==False:
    print("Error connecting to mysql database")
cursor=mycon.cursor()
#giving sql query
cursor.execute("select * from stu_info")
#fetching only first row
data =cursor.fetchone()
count=cursor.rowcount
print("Total number of rows retrieved so far from resultset:",count)
for row in data:
    print(row)
print("----------------------------")
#fetching next 4 rows
data =cursor.fetchmany(4)
count=cursor.rowcount
print("Total number of rows retrieved so far from resultset:",count)
for row in data:
    print(row)
print("----------------------------")

    
