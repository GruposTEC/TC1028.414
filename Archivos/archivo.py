#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 26 17:51:57 2020

@author: avmejia
"""

def lectura(arch,renglon,elemento):
    f = open(arch,'r')
    lista = []
    linea = f.readline()
    while linea:
        linea = linea.strip()
        linea = linea.split(',')
        for i in range(len(linea)):
            linea[i] =int(linea[i])
        lista.append(linea)
        print(linea)
        linea = f.readline()
    f.close()
    print(lista)
    return(lista[renglon][elemento])
    
lectura("informacion.txt",2,2)
    