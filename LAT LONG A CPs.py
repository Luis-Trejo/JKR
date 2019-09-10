# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 15:59:55 2019

@author: Kike
"""

import csv
import os


for i in range(2,32):
    mainpath = "D:/CPs/"
    filename = str(i) + ".csv"
    fullpath = os.path.join(mainpath, filename)
    
    input_file = csv.DictReader(open(fullpath))

    PLL = None
    PF = []
    LR = []
    for row in input_file:
        PLL = str(row["ns1:coordinates"])
        PF = PLL.split(","),row["ns1:SimpleData"],row["ns1:name"] 
        Corr = PF[0]
        r = (PF[0][1])
        x = 0    
        for i in Corr:
        
            registro = [Corr[x], PF[1], PF[2], r[0:17], r[19:37]]
            LR.append(registro) 
            x = x + 1
        



    with open(filename, 'w', newline='') as fp:
        a = csv.writer(fp, delimiter=',')
        a.writerows(LR)
    
print("Archivos Generados")

