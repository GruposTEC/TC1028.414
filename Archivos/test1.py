#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest

import archivo


class Testprueba (unittest.TestCase):

    def test_codificacion(self):
        self.assertEqual(archivo.lectura("informacion.txt",1,2),7)
        self.assertEqual(archivo.lectura("informacion.txt",2,3),12)
        
if __name__ == '__main__':
    unittest.main()
