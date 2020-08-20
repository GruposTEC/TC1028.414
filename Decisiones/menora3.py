#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 19 13:41:40 2020

@author: avmejia
"""

#Recibir Primera moneda;
#recibir Segunda moneda;
#Recibir Tercera moneda;
#if moneda1 < moneda2{
#  menor es la moneda 1;
#  imprimo que la menor es la moneda1;
#}
#else{
#  menor es la moneda 2;
#  imprimo que la menor es la momneda2
#}
#if moneda3 < menor{
#  menor es la moneda 3
#}
#Imprimir cual es la menor;

mon1 = float(input())
mon2 = float(input())
mon3 = float(input())

if mon1 < mon2  and mon1 < mon3:
    menor = mon1
    print(f'La menos hasta ahora  es : {menor}')
elif mon1 == mon2:
    menor = mon1    
else:
    menor = mon2
    print(f'La menos hasta ahora  es : {menor}')
if mon3 < menor :
    menor = mon3

print(f'La menor de 3 es {menor}')


