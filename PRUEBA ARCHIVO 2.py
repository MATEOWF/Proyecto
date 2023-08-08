# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 18:59:10 2023

@author: Mateo Farinango
"""

archivo=open("devices.txt")
for item in archivo:
    item=item.strip()
    print(item)
archivo.close()
    
