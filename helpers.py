# Description: Helper functions for the main program

import re
import os
import platform


def limpiar_pantalla():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')


def leer_texto(longitud_min=0, longitud_max=100, mensaje=None):
    print(mensaje) if mensaje else None
    while True:
        texto = input("> ")
        if len(texto) >= longitud_min and len(texto) <= longitud_max:
            return texto
        

def modelo_valido(modelo, lista):
    if not re.match('[a-zA-Z][0-9]$', modelo):
        print("Modelo incorrecto, debe cumplir el formato.")
        return False
    for vehiculo in lista:
        if vehiculo.modelo == modelo:
            print("Modelo utilizado por otro vehículo.")
            return False
    return True

def ruedas_valido(ruedas):
    if not ruedas == 2 and not ruedas == 4:
        print("Ruedas incorrecto, todos los vehiculos tienen 2 o 4 ruedas.")
        return False
    return True
            
