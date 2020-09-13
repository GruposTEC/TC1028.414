#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  5 18:38:00 2020

@author: avmejia
"""

import unittest
import etapa
import busqueda_numero


class Testprueba (unittest.TestCase):

    def test_etapa(self):
        self.assertEqual(etapa.es_edad(15),"adolescente")
        self.assertEqual(etapa.es_edad(2),"huerco")
        self.assertEqual(etapa.es_edad(25),"adulto")
        self.assertEqual(etapa.es_edad(65),"mayor")
        self.assertEqual(etapa.es_edad(8),"chico")
        
    def test_medio(self):
        self.assertEqual(busqueda_numero.encontrar_el_medio(15,10,30),15)
        self.assertEqual(busqueda_numero.encontrar_el_medio(1,2,3),2)
        self.assertEqual(busqueda_numero.encontrar_el_medio(11,12,15),12)
        
       




if __name__ == '__main__':
    unittest.main()