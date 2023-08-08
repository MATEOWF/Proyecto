# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 19:27:24 2023

@author: Mateo Farinango
"""

archivo=open("devices.txt","a") 
while True:
    newitem=input("Ingrese el nuevo dispositivo: ")
    if newitem =="exit":
     print("Todo listo")
    break
    archivo.write(newitem + "\n")
archivo.close()
    
print(archivo)
    