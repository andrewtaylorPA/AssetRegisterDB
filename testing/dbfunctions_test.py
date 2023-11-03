import pytest

from Code import dbfunctions

def test_recordManual():
    assert dbfunctions.recordManual('DV00112','WWWWW','Latitude 1234','High Spec Laptop','Andy Taylor','IT','IT','9000','01/01/2022','Active') == "INSERT INTO AssetRegister (Hostname,AssetTag,Description,DeviceType,CurrentUser,Department,CostCentre,CostCode,PurchaseDate,Status) VALUES ('DV00112','WWWWW','Latitude 1234','High Spec Laptop','Andy Taylor','IT','IT','9000','01/01/2022','Active')"

def test_searchAll():
    assert dbfunctions.searchAll('Status','Storage') == "('DV00145', 'WWWWWW', 'Optiplex 3010', 'High Spec Desktop', 'David Johnson', 'Racing', 'Racing Operations', '7000', '10/04/2019', 'Storage')"
    
