# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 22:05:03 2023

@author: Mateo Farinango
"""

#BASIC DATA TYPES
type(90) #INT ENTERO
type(9.85) # FLOAT FLOTANTE
type("HOLA") # STR TEXTO
type(True) # BOOL


#COMPARACION
2<3
3>5
1==1
1>=1
1<=1

#CREACION DE VARIABLE

x=3
x*5
x-3
"CISCO" * x
" CISCO " * 2 

#CONCATENAR VARIABLES
str1="Cisco"
str2="Networking"
str3="Academy"
space=" "
print(str1+space+str2+space+str3)
#USO DE LA COMA 
print(str1,str2,str3)

#CONVERTIR TIPOS DE DATOS

x=3
print("EL valor de x es"+ x)

print("El valor de x es " + str(x))

type(x)

#OTRO EJERCICIO

pi=22/7
print(pi)
print("{:.2f}".format(pi))
print("{:.9f}".format(pi))
