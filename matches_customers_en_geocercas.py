# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 14:03:34 2019

@author: Kike
"""


import csv
import os
import pandas as pd

mainpath = "D:/"
filename = "testmatch.csv"
fullpath = os.path.join(mainpath, filename)

file = csv.DictReader(open(fullpath))

matches = [["Geo","id1","id2", "Concate"]]


## Forma 2
for row in file:
    print(row)
    g = row["Geohash"]
    a = row["id_customer"]
    print(a + g)
    for row in file2:
        g2 = row["Geohash"]
        a2 = row["id_customer"]
        if g == g2 and a != a2:
           con = g + a + a2 
           registro = [g, a, a2, con]
           matches.append(registro)
           print(registro)
    file2 = csv.DictReader(open(fullpath))
    
for row in matches:
    print(row)
    
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


## Eliminando con funcion
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
    
## Eliminando Duplicidades de la forma 2
print(matches[2][1])
n = 1
for row in matches:
    a = matches[n][1]
    b = matches[n][2]
    int(a)
    int(b)
    r = 1
    for row in matches:
        c = matches[r][1]
        d = matches[r][2]
        int(c)
        int(d)
        x = a + b
        print(x)
        y = c + d
        print(y)
        if x == y:
            print(x,y)
            matches.remove(row)
  

for row in matches:
    print(row)


## Escribir Resultados  
             
with open("output.csv", mode = 'w') as f:
    writer = csv.writer(f)
    writer.writerows(matches)


## Forma 1
match = 0
for row in file:
  a = row["id_customer"]
  g = row["Geohash"]
  for row in file2:
    b = row ["id_customer"]
    if a != b:
        for row in file3:
            if g == row["Geohash"]:
                n = row["id_customer"]
                if n == a or n == b:
                   match = match + 1
                   registro = [a,b,g,match]
                   matches.append(registro)
        file3 = csv.DictReader(open(fullpath))
        match = 0
  file2 =  csv.DictReader(open(fullpath)) 
print(matches)

## Forma 3 no jala

for row in file:
    print(row)
    g = row["Geohash"]
    a = row["id_customer"]
    print(a + g)
    for row in file2:
        g2 = row["Geohash"]
        a2 = row["id_customer"]
        if g == g2 and a != a2: 
           n = 0 
           for i in matches:
               a3 = matches[n][1]
               a4 = matches[n][2]
               if a3 == a or a3 == a2 and a4 == a or a4 == a2:
                   print("registro ya existe")
               else:    
                   registro = [g,a,a2]
                   matches.append(registro)
                   n = n + 1 
                   print(registro)
                                           
    file2 = csv.DictReader(open(fullpath))



            
            
    
help(csv.writer)