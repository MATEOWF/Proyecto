# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 20:10:02 2023

@author: Mateo Farinango
"""

# -*- coding: utf8 -*-



from tostadas_pipo.utilidades import calculos
from tostadas_pipo.utilidades.impuestos import impuesto_iva14

monto = int(input("Introduzca un monto entero: "))
monto_suma = int(input("Introduzca un monto entero a sumar: "))

suma = impuesto_iva14(monto) + calculos.suma_total(monto_suma)

print("Total a Facturar: {0} BsS, con IVA 14%.".format(suma))
 


