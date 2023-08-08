# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:16:10 2023

@author: Mateo Farinango
"""

lista=[]
archivo=open("devices.txt")
for item in archivo:
    item=item.strip()
    lista.append(item)
    print(item)
archivo.close()


print(lista)






