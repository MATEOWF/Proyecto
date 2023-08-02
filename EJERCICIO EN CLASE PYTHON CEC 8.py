# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:38:47 2023

@author: Mateo Farinango
"""

# TALLER CON EDAD Y USO DE ELIF 
print("IDENTIFICACION DE EDAD")
edad=int(input("Ingrese su edad:"))
if edad>=1 and edad<=10:
    print("la persona es un infante")
elif edad>10 and edad<=17:
    print("La persona es un adolescente")
elif edad>17 and edad<=25:
    print("La persona es un adulto mayor joven")
elif edad>25 and edad<=60:
    print("La persona es un adulto mayor maduro")
elif edad>60 and edad<=100:
    print("La persona es de la tercera edad")
else:
    print("La edad ingresada supera lo convencional")

    
