import pyodbc

def dbConnection():
    global conn
    global cur
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};Server=DV00484\SQLEXPRESS;UID=andyt;PWD=dbpassword;'
    conn = pyodbc.connect(connectionString) # connects to the db using the above connection string
    cur = conn.cursor() # This manages the command that we want to send - cursor = invoke-command

def dbCommit():
    conn.commit()

def dbClose():
    conn.close

def recordManual(Hostname,AssetTag,Description,DeviceType,CurrentUser,Department,CostCentre,CostCode,PurchaseDate,Status):
    dbConnection()
    global sqlqueryvar
    print("Function to manually add data to database")
    
    print("Inporting record into database")
    sqlqueryvar = ("INSERT INTO AssetRegister (Hostname,AssetTag,Description,DeviceType,CurrentUser,Department,CostCentre,"
                   "CostCode,PurchaseDate,Status) VALUES ('" + Hostname + "','" + AssetTag + "','" + Description + "',"
                   "'" + DeviceType + "','" + CurrentUser + "','" + Department + "','" + CostCentre + "','" + CostCode + "',"
                   "'" + PurchaseDate + "','" + Status + "')")
    print(sqlqueryvar)
    cur.execute(sqlqueryvar)
    print("Committing record to database")
    #conn.commit()
    print("Returning to menu")
    return sqlqueryvar

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
    global ResultList
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
    ResultOutput = ''.join(str(x) for x in ResultList)
    return ResultOutput
    

def finish():
    
    return "Exiting"