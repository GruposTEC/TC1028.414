# -*- coding: utf-8 -*-
"""
Created on Wed Aug 26 10:00:37 2020

@author: Antonio
"""

"""
Método Calcula precio sin descuento;
asigno el precio de la silla básica;
Asigno el precio de la silla Estandar;
Asigno le precio de la silla de lujo;
if tipo de silla = 'b'{
  el precio es la cantidad de sillas por el precio de la
  básica;
}
if tipo de silla es 'e'{
  el precio es la cantidad de sillas por el precio de la estandar;
}
if tipo de silla es 'l'{
  el precio es la cantidad de sillas por el precio de la lujo;
}
Regreso el precio calculado;"
"""

def calcula_precio_antes_descuento(cantidad, tipo):
    """
    Método que calcula el precio de venta antes de aplicar cualquier
    descuento, basándose en la cantidad de sillas y de que tipo es    

    Parameters
    ----------
    cantidad : int
        Cantidad de sillas a vender.
    tipo : str
        Letra que indica el tipo de silla , básica (B) , estandar (E)
        lujo (L).

    Returns
    -------
    precio : int
        El precio de venta.

    """
    basica = 700
    estandar = 900
    lujo = 1500
    
    if tipo == 'B':
        precio = basica * cantidad
    if tipo == 'E':
        precio = estandar * cantidad
    if tipo == 'L':
        precio = lujo * cantidad
    
    return precio

"""
Método Calcula_precio_despues_descuento; // recibo el precio a calcular el descuento y el tipo de cliente
if cliente es 'N'{
  if precio >= 10000 y precio < 20000{
    tasa es igual a 10%
  }
  if precio mayor a 20000{
    tasa es igual al 15%
  }
  if precio es menor a 10000{
    tasa es igual a 0%
  }
}
if cliente es iaugal a 'F'{
  tasa es igual al 20%
}
El descuento es el precio por la tasa;
Regreso el descuento calculado;
"""
    
def calcula_precio_despues_descuento(precio,cliente):
    """
    Método que caldula dependiendo del monito a vender y el tipo de cliente
    el monto del descuento que se aplicará  en la venta

    Parameters
    ----------
    precio : int
        El precio sin descuento de la venta.
    cliente : str
        Tipo de cliente normal (N) VIP (F).

    Returns
    -------
    descuento : int
        el descuento calulaod por precio y tipo de clietne.

    """
    
    if cliente =='N':
        if precio  >= 10000 and precio < 20000 :
            tasa = .1
        if precio > 20000:
            tasa = .15
        if precio < 10000:
            tasa= 0 
    if cliente == "F" :
        tasa = .2
        
    descuento = precio*tasa    
    
    return descuento

"""
Función main;
Recibo el tipo de silla;
Recibo el tipo de cliente;
recibo la cantidad de sillas;
Calculo el precio antes del descuento; //es un método
Calculo el precio después del descuento; //es un método
Imprimo el precio antes del descuento
Impirmo el descuento;
Imprimo el precio final;
Fin;
"""

def main():
    tipo_silla = input()
    tipo_cliente = input()
    cantidad =int(input())

    pad = calcula_precio_antes_descuento(cantidad, tipo_silla)   
    descuento = calcula_precio_despues_descuento(pad,tipo_cliente)
    preciofinal = pad-descuento
    
    print(pad)
    print(descuento)
    print(preciofinal)
    
    
main()    
    