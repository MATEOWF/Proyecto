# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:56:14 2023

@author: Mateo Farinango
"""

# while

contar=input("Ingrese al numero al que desea contar: ")
contar=int(contar)
contador=1
while contador<=contar:
    print(contador)
    contador+=1
    if contador> contar:
        break
        



