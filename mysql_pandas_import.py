#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:40:36 2017

@author: vishesh
"""


import mysql.connector as sql
import pandas as pd



#MySQL
configGrizzly = {
  'user': 'vishesh.kochher',
  'password': ‘xxxxxx’,
  'host': ‘host.host.com’,
  'database': ‘dynamo’
}

cnx = sql.connect(**configGrizzly)


cursor = cnx.cursor()

df = pd.read_sql("SELECT * from Account" ,con = cnx)
#cursor.execute(query)


cursor.close()


cnx.close()

dfnames = df.loc[:,("id","firstname", "lastname")]

print(dfnames[:10])