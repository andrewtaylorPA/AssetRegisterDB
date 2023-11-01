from re import search
import pyodbc

connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};Server=DV00484\SQLEXPRESS;UID=andyt;PWD=dbpassword;'
conn = pyodbc.connect(connectionString) # connects to the db using the above connection string
cur = conn.cursor() # This manages the command that we want to send - cursor = invoke-command
"""
insertrows = ["INSERT INTO AssetRegister (Hostname,AssetTag,Description,DeviceType,CurrentUser,Department,CostCentre,CostCode,PurchaseDate,Status) VALUES ('DV00484','7GJP7C3','Latitude 5420','High Spec Laptop','Andy Taylor','IT:Desktop Support','IT:Desktop Support','9000','01/03/2021','Active')"]

print("Inserting rows")
for record in insertrows:
    print(record)
    cur.execute(record)

"""

def recordManual(Hostname,AssetTag,Description,DeviceType,CurrentUser,Department,CostCentre,CostCode,PurchaseDate,Status):
    print("Function to manually add data to database")
    
    print("Inporting record into database")
    sqlqueryvar = ("INSERT INTO AssetRegister (Hostname,AssetTag,Description,DeviceType,CurrentUser,Department,CostCentre,"
                   "CostCode,PurchaseDate,Status) VALUES ('" + Hostname + "','" + AssetTag + "','" + Description + "',"
                   "'" + DeviceType + "','" + CurrentUser + "','" + Department + "','" + CostCentre + "','" + CostCode + "',"
                   "'" + PurchaseDate + "','" + Status + "')")
    cur.execute(sqlqueryvar)
    print("Committing record to database")
    conn.commit()

    return sqlqueryvar
    print("Returning to menu")

def csvImport():
    print("")    
    print("This is the CSV Import function")
    print("")
    
    Assetslist = []

    AssetsFile = open("C:/Users/andyt/QAUnit/AssetRegisterDB/Data/Assets.csv")
    AssetsToAdd = AssetsFile.readlines()
    AssetsFile.close()
    print(AssetsToAdd)

    for line in AssetsToAdd:
        line = line.strip()    
        Assets = line.split(",")
        print(Assets)
        Assetslist.append(Assets)
    
    index = 0
    
    for Assets in Assetslist:
        sqlstring = ("INSERT INTO AssetRegister (Hostname,AssetTag,Description,DeviceType,CurrentUser,"
                     "Department,CostCentre,CostCode,PurchaseDate,Status)"
                     "VALUES ('" + Assetslist[index][0] + "','" + Assetslist[index][1] + "','" + Assetslist[index][2] + "',"
                     "'" + Assetslist[index][3] + "','" + Assetslist[index][4] + "','" + Assetslist[index][5] + "',"
                     "'" + Assetslist[index][6] + "','" + Assetslist[index][7] + "','" + Assetslist[index][8] + "',"
                     "'" + Assetslist[index][9] + "')")
        index = index + 1
        try:
            cur.execute(sqlstring)
            conn.commit()
        except Exception as e:
            print(e)
            
    print("")
    print("CSV Import Success")
    print("")

def searchHostname():
    Hostname = input("Enter a hostname to search: ")
    sqlquery = "SELECT * FROM AssetRegister WHERE Hostname='" + Hostname + "'"
    try:
        result = cur.execute(sqlquery).fetchall()
        for row in result:
            print(row)
            print("")
    except Exception as e:
        print(e)

def searchAll(searchQuery,searchValue):
    sqlquery = "SELECT * FROM AssetRegister WHERE " + searchQuery + "='" + searchValue + "'"
    print("")
    print("SQL Query = " + sqlquery)
    try:
        results = cur.execute(sqlquery).fetchall()
        ResultList = []
        for row in results:
            print ("")
            ResultList.append(row)
    except Exception as e:
        print(e)
    return ResultList
    

def finish():
    
    return "Exiting"



selection = 10

while selection != 0:
    print("Asset Register Menu")
    print("")
    print("1 - Manual inport")
    print("2 - CSV Import")
    print("3 - Search")
    print("0 - Exit")
    print("")
    selection = int(input("Please choose a process: "))
        
    if selection == 1:
        print("Function to manually add data to database")
        print("Please enter the following information:")
        Hostname = input("Hostname: ")
        AssetTag = input("AssetTag: ")
        Description = input("Description: ")
        DeviceType = input("Device Type: ")
        CurrentUser = input("Current User: ")
        Department = input("Department: ")
        CostCentre = input("Cost Centre: ")
        CostCode =  input("Cost Code: ")
        PurchaseDate = input("Purchase Date: ")
        Status = input("Status: ")
       
        print("The details you entered are:")
        print(Hostname)
        print(AssetTag)
        print(Description)
        print(DeviceType)
        print(CurrentUser)
        print(Department)
        print(CostCentre)
        print(CostCode)
        print(PurchaseDate)
        print(Status)
    
        correct = input("Are the above details correct? - Yes/No: ")
        if correct.lower() == 'yes':
            recordManual(Hostname,AssetTag,Description,DeviceType,CurrentUser,Department,CostCentre,CostCode,PurchaseDate,Status)
        else:
            print("Returning to menu, please enter the correct details")
            
    if selection == 2:
        csvImport()
    if selection == 3:
        print("Hostname")
        print("AssetTag")
        print("Description")
        print("DeviceType")
        print("CurrentUser")
        print("Department")
        print("CostCentre")
        print("CostCode")
        print("PurchaseDate")
        print("Status")    
        searchQuery = input("Select a query field from above: ")
        searchValue = input("Enter the value to search: ")
        mySearchResults = searchAll(searchQuery,searchValue)
        print(mySearchResults)
        print("")
    if selection == 0:
        finish()

conn.close()