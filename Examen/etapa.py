#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 14:55:32 2020

@author: avmejia
"""
def es_edad(edad):
    if edad < 2:
        return "bebé"
    if edad >= 2 and edad < 4 :
        return "huerco"
    if edad >= 4 and edad < 13 :
        return "chico" 
    if edad >= 13 and edad < 20 :
        return "adolescente"
    if edad >= 20 and edad < 65 :
        return "adulto"
    if edad >= 65 :
        return "mayor"
    
    