#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 21 14:45:14 2020

@author: avmejia
"""
"""
codificacion (mensaje, llave);
creo la variable respuesta como string vacio;
for(cada letra dentro del mensaje){
    convierto la letra a ascii guardandola en la variable masc;
    sumo la llave a la variables masc;
    convierto masc a letra;
    agrego la nueva letra a la respuesta;}
regreso la respuesta;
"""


def codificacion_cesar(mensaje,llave):
    """
    Método que codifica mediante cifrado cesar

    Parameters
    ----------
    mensaje : str
        mensaje a encriptar.
    llave : int
        desplazamiento usado en el encriptamiento.

    Returns
    -------
    respuesta : str
        mensaje encriptado.

    """
    respuesta = ""
    for i in mensaje:
        masc = ord(i)
        masc = masc + llave
        letra = chr(masc)
        respuesta = respuesta + letra
    return respuesta

"""
codificacion (mensaje, llave);
creo la variable respuesta como string vacio;
for(cada letra dentro del mensaje){
    convierto la letra a ascii guardandola en la variable masc;
    sumo la llave a la variables masc;
    convierto masc a letra;
    agrego la nueva letra a la respuesta;}
regreso la respuesta;
"""

def decodificacion_cesar(mensaje,llave):
    """
    Método que codifica mediante cifrado cesar

    Parameters
    ----------
    mensaje : str
        mensaje a desencriptar.
    llave : int
        desplazamiento usado en el desencriptamiento.

    Returns
    -------
    respuesta : str
        mensaje encriptado.

    """
    respuesta = ""
    for i in mensaje:
        masc = ord(i)
        masc = masc - llave
        letra = chr(masc)
        respuesta = respuesta + letra
    return respuesta

print(codificacion_cesar("Hola a todos",3))
print(decodificacion_cesar("Krod#d#wrgrv",3))