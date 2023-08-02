# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 17:20:46 2023

@author: Mateo Farinango
"""
# LISTA, IF Y FOR 

listar=[]
lista=["R1","R2","R3","S1","S2","S3","AP1","AP2","AP3","FW1","PC2","FW4"]
for elemento in lista:
    if "R" in elemento:
        print(elemento)

for elemento in lista:
    if "R" in elemento:
        listar.append(elemento)
        
print(listar)        

# OTRO EJERCICIO

lista_r=[]
lista_s=[]
lista_ap=[]
lista_otro=[]
for i in lista:
    if "R" in i:
        lista_r.append(i)
    elif "S" in i:
        lista_s.append(i)
    elif "AP" in i:
        lista_ap.append(i)
    else:
        lista_otro.append(i)
        

print(lista_r)
print(lista_s)
print(lista_ap)
print(lista_otro)



