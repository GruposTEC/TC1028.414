#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:53:37 2020

@author: avmejia
"""

import math

def area_cilindro (radio, altura):
    return 2 * math.pi * radio * altura + 2 * math.pi * math.pow(radio,2)

def volumen_cilindro (radio, altura):
    return  math.pi *  math.pow(radio,2) * altura

            
area = area_cilindro (3.3,1.3)
volumen = volumen_cilindro (3.3,1.3)
print ("area=%f" %area)
print ("volumen=%f" %volumen)


#Python 3.8.2 (default, Feb 26 2020, 02:56:10)
   
#area=52.768703
#volumen=22.320287
    