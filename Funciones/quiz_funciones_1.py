#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 16:46:01 2020

@author: avmejia
"""

def uno (a, b):
    a = a // 3    
    return a + b


def main():    
    x = 10    
    y = 40    
    z = uno(y, x)    
    print(z)
    
main()