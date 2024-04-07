#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 10 22:44:59 2024
@author: jorge
"""
from pantalla import clear_screen

def space():
    print("\n")

def fusion():
    #Crea un diccionario a partir de dos cadenas
    paises = ["Peru","Chile","Bolivia","Argentina"]
    capitales = ["Lima","Santiago","Sucre","Buenos Aires"]
    res = dict(zip(paises, capitales)) # poderosisima funcion
    print(res)    

clear_screen()
space()
print("Listado De Paises y Capitales")
print("-------------------------------------")
fusion()
space()

        