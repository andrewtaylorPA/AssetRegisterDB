
from dbfunctions import dbConnection, dbCommit, dbClose, searchAll, recordManual, csvImport, searchHostname, finish
import pyodbc

dbConnection()

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
            dbCommit()
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
        print("Results are: ")
        print(mySearchResults)
        print("")
    if selection == 0:
        finish()

dbClose()