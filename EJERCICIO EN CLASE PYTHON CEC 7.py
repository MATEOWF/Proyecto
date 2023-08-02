# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 16:12:33 2023

@author: Mateo Farinango
"""

# IF Y ELSE 
datos=100
nativa=1
if datos==nativa:
    print("Las VLAN son iguales")
else:
    print("Las VLAN son diferentes")
    
# EJERCICIO CON EDAD E INPUT

edad=int(input("Ingrese la edad:"))    
print(edad)
if edad>=18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
    
# USO DEL ELIF
acl=int(input("Ingrese el # de ACL"))
if acl>=1 and acl<=99:
    print("Es una ACL Estandar")
elif acl>=100 and acl<=199:
    print("Es una ACL Extendida")
else:
    print("El # Ingresado no es una ACL")
    