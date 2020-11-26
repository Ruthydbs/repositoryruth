# repositoryruth
ceci est un test oe

boh

import pypyodbc as pyodbc
import sys
conn = pyodbs.connect('Driver={SQL Server};'
               'Server=LAT3510-2\SQL;
               'Database=Aliexpress;
               'Trusted_Connection=yes;)




cursor = conn.cursor()
cursor.execute("""INSERT INTO Fournisseurs (IdF,NomF,VilleF,AdrF,TelF) values (1,'Ruth','Paris','Creteil','*****')""")
cursor.execute("""INSERT INTO Fournisseurs (IdF,NomF,VilleF,AdrF,TelF) values (2,'Yasmine','Vitry','vitry','$$$$$')""")
cursor.execute("""INSERT INTO Fournisseurs (IdF,NomF,VilleF,AdrF,TelF) values (3,'alae','maroc','maison','*0*')""")
cursor.execute('select * from Fournisseurs')

for row in cursor:
    print(row)
