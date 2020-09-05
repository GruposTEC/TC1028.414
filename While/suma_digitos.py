#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 09:32:45 2020

@author: avmejia
"""
def suma_digitos(numero):
    digito=0
    suma=0
    while(numero!=0):
        digito = numero % 10
        suma = suma + digito
        numero = numero // 10
    return suma
        
        
main():
    numero = int(input()) 
    solucion = suma_digitos(numero)
    print(solucion)
    
main()    

