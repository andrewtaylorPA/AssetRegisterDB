import pyodbc
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};Server=DV00484\SQLEXPRESS;UID=andyt;PWD=dbpassword;'
conn = pyodbc.connect(connectionString) # connects to the db using the above connection string
cur = conn.cursor() # This manages the command that we want to send - cursor = invoke-command


# CREATE TABLE statement

# CREATE TABLE table_name (
#    column1 datatype constraint,
#    column2 datatype constraint,
#    column3 datatype constraint,
#   ....
#); 

print("Dropping table")
dropstring = "DROP TABLE AssetRegister"
cur.execute(dropstring)

print("Creating Asset Register table")
sqlstring = "CREATE TABLE AssetRegister ( Hostname nvarchar(10) NOT NULL PRIMARY KEY, AssetTag nvarchar(10) NOT NULL, Description nvarchar(30) NULL, DeviceType nvarchar(30) NULL, CurrentUser nvarchar(30) NULL, Department nvarchar(40) NULL, CostCentre nvarchar(40) NOT NULL, CostCode nvarchar(10) NOT NULL, PurchaseDate nvarchar(10) NOT NULL, Status nvarchar(20) NULL)"
cur.execute(sqlstring)

"""
insertrows = ["INSERT INTO Student (Hostname,AssetTag,Description,DeviceType,Current User,Department,CostCentre,CostCode,PurchaseDate,Status) VALUES (DV00484,'7GJP7C3','Latitude 5420','High Spec Laptop','Andy Taylor',IT:Desktop Support,IT:Desktop Support,9000,01/03/2021,Active)",]

print("Inserting rows")
#for record in insertrows:
    #cur.execute(record)
    #conn.commit()

print("Updating records")
sqlqueryvar = "UPDATE Student SET City = 'Doncaster' WHERE StudentID = 5"
#cur.execute(sqlqueryvar)
#conn.commit()

studentlist = []

StudentsFile = open("python/students.csv")
StudentsToAdd = StudentsFile.readlines()
StudentsFile.close()
print(StudentsToAdd)

for line in StudentsToAdd:
    student = line.split(",")
    print(student)
    studentlist.append(student)

print("Student list index 0")
print(studentlist[0][1])

index = 1

for student in studentlist:
    sqlstring = "INSERT INTO Student (StudentID, FirstName,Surname,Course,City) VALUES ("+ str(index) + ",'" + studentlist[0][0] + "','" + studentlist[0][1] + "','" + studentlist[0][2] + "','" + studentlist[0][3] + "')"
    index = index + 1
    print(sqlstring)
    try:
        cur.execute(sqlstring)
    except Exception as e:
        print(e)
        
"""
conn.commit()


conn.close()
