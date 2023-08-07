# -*- coding: utf-8 -*-
"""
Created on Thu Aug  3 19:52:17 2023

@author: Mateo Farinango
"""

def badFun(n):
    try:
        return n / 0
    except:
        print("Error en cualquier parte")
        raise 
try:
    badFun(0)
except ArithmeticError:
    print("Error lanzado por raise")
print("THE END.")


