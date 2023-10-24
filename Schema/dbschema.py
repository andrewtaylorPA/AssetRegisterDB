import pyodbc
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};Server=DV00484\SQLEXPRESS;UID=andyt;PWD=dbpassword;'
conn = pyodbc.connect(connectionString) # connects to the db using the above connection string
cur = conn.cursor() # This manages the command that we want to send

print("Dropping table")
dropstring = "DROP TABLE AssetRegister"
cur.execute(dropstring)

print("Creating Asset Register table")
sqlstring = "CREATE TABLE AssetRegister ( Hostname nvarchar(10) NOT NULL PRIMARY KEY, AssetTag nvarchar(10) NOT NULL, Description nvarchar(30) NULL, DeviceType nvarchar(30) NULL, CurrentUser nvarchar(30) NULL, Department nvarchar(40) NULL, CostCentre nvarchar(40) NOT NULL, CostCode nvarchar(10) NOT NULL, PurchaseDate nvarchar(10) NOT NULL, Status nvarchar(20) NULL)"
cur.execute(sqlstring)

conn.commit()

conn.close()
