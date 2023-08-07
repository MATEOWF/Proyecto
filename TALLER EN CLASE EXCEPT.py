# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 20:07:14 2023

@author: Mateo Farinango
"""

def readint(prompt, min, max):
    while True:
        try:
            valor = int(input(prompt))
            if min <= valor <= max:
                return valor
            else:
                print("Error: el valor no está en el rango permitido ({min}..{max})")
        except ValueError:
            print("Error en el ingreso")

# USP
v = readint("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)


#SOLUCION DEL EJERCICIO

def validarNumero(prompt,min,max):
    while(True):
        try:
            print("Ingrese un valor entre ",min,"y",max)
            x=int(input(prompt))
            assert x >= min and x<=max
            return x
        except ValueError:
            print("Ingresar solo numero:")
        except:
            print("Error,el valor debe estar dentro del rango")

v=validarNumero("Ingrese un valor en el rango: ",-100,100)

print("El numero es: ",v)
