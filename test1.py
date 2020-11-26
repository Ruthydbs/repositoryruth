#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Thu Nov 26 15:44:29 2020

@author: ruthydubois
"""

import pyodbs
conn = pyodbs.connect('Driver={SQL Server};'
               'Server=DESKTOP-IKJ0O3E\SQLEXPRESS;'
               'Database=Aliexpress;'
               'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute("""INSERT INTO Fournisseurs (IdF,NomF,VilleF,AdrF,TelF) values (1,'Ruth','Paris','Creteil','*****')""")
cursor.execute("""INSERT INTO Fournisseurs (IdF,NomF,VilleF,AdrF,TelF) values (2,'Yasmine','Vitry','vitry','$$$$$')""")
cursor.execute("""INSERT INTO Fournisseurs (IdF,NomF,VilleF,AdrF,TelF) values (3,'alae','maroc','maison','*0*')""")
cursor.execute('select * from Fournisseurs')

for row in cursor:
    print(row)
    

conn.commit()