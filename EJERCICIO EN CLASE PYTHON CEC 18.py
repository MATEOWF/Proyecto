# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:47:55 2023

@author: Mateo Farinango
"""

#LABORAOTRIO EJERCICIO EN CLASE WORD 
import math

def EsPrimo(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    
    # Calcular la raíz cuadrada de num y convertirla a entero
    limite = int(math.sqrt(num)) + 1
    
    # Verificar si el número es divisible por algún primo en la lista
    for primo in primos:
        if primo >= limite:
            break
        if num % primo == 0:
            return False
    
    return True

primos = []

# Prueba de la función con números del 1 al 20
for i in range(1, 21):
    if EsPrimo(i):
        primos.append(i)

print(primos)