# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:39:24 2023

@author: Mateo Farinango
"""

class Coche:
    def __init__(self, marca, modelo, ano, color, kilometraje):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.color = color

    def encendido(self):
        print(f"El coche {self.marca} {self.modelo} se encendió.")

    def apagado(self):
        print(f"El coche {self.marca} {self.modelo} se apagó.")


        
        
        
        
        
        
        