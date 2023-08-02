# -*- coding: utf-8 -*-
"""
Created on Tue Aug  1 19:07:33 2023

@author: Mateo Farinango
"""

def funlista(lista):
    for item in lista:
        print("Hola",item)
    print(" ")
 

funlista(["Juan"])
funlista(["Juan","Jorge"]) 


def suma(*a):
    print("\nTipo de datos argumento:",type(a))
    sum=0
    for n in a:
     sum +=n
    print("Suma",sum)
    

suma(1,5)
suma(1,5,6,8,10)    
    
    
        