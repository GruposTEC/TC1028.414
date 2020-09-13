#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 19:17:09 2020

@author: avmejia
"""
def mayor(uno,dos,tres):
    if uno > dos:
        valor = uno
    else:
        valor = dos
    if tres > valor:
        valor = tres
    
    return valor

def menor(uno,dos,tres):
    if uno < dos:
        valor = uno
    else:
        valor = dos
    if tres < valor:
        valor = tres
    
    return valor


def encontrar_el_medio(uno,dos,tres):
    
    grande = mayor(uno,dos,tres)
    chico = menor(uno,dos,tres)
    
    if uno != grande and uno !=chico:
        return uno
    if dos != grande and dos !=chico:
        return dos
    if tres != grande and tres !=chico:
        return tres
    
