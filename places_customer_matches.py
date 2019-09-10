# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 12:07:56 2019

@author: Kike
"""

import psycopg2
import time
import pandas as pd
import pandas.io.sql as sqlio
import csv
import os


con_string = "dbname=yopterdwh host=yopter.ccyy9l6xansm.us-east-1.redshift.amazonaws.com port=5439 user=yopter password=R3x1q3tjk"
con=psycopg2.connect(con_string)
cur = con.cursor()


##Extraccion de todas las interacciones de customers almacenados en tabla familias(que comparten vivienda)

cur.execute('CREATE TABLE analytics.matches as SELECT id_customer, geohash from analytics.customer_place_denue where id_customer IN (SELECT id_customer from analytics.familias_model);')
con.commit()

sql = "select count (id_customer) from analytics.matches;"
dat = sqlio.read_sql_query(sql, con)
dat

sql = "select count(id_customer) from analytics.familias_model;"
dat = sqlio.read_sql_query(sql, con)


sql = "select * from analytics.matches;"
dat = sqlio.read_sql_query(sql, con)
dat.to_csv('matches.csv')



## Creando matches todos los matches de estos customers


file = csv.DictReader(open('matches.csv'))
file2 = list(csv.DictReader(open('matches.csv')))



matches = [["Geo","id1","id2", "Concate"]]

## Generando Matches
for row in file:
    g = row["geohash"]
    a = row["id_customer"]
    for row in file2:
        g2 = row["geohash"]
        a2 = row["id_customer"]
        if g == g2 and a != a2:
           con = g + a + a2 
           registro = [g, a, a2, con]
           matches.append(registro)



## funcion verificar pertmutaciones
def is_perm_1(str_1, str_2):
    str_1 = str_1.lower()
    str_2 = str_2.lower()

    if len(str_1) != len(str_2):
        return False

    str_1 = ''.join(sorted(str_1))
    str_2 = ''.join(sorted(str_2))

    n = len(str_1)

    for i in range(n):
        if str_1[i] != str_2[i]:
            return False
    matches.remove(row)


## Eliminando observaciones duplicadas con funcion
p = 1
for row in matches:
        try:
            a = matches[p][3]
            q = 2
            for row in matches:
                try:
                    b = matches[q][3]
                    is_perm_1(a,b)
                    q = q + 1
                except: 
                        print("next")
        except:
            print("archivo terminado")
        p = p + 1
con.close()