import re
import os
import platform

def limpiar():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def numero_ruedas():
    while True:
        try:
            ruedas = int(input('Introduce el número de ruedas: '))
            if ruedas < 0:
                print('El número de ruedas no puede ser negativo')
            else:
                return ruedas
        except ValueError:
            print('El número de ruedas debe ser un número entero')

def color():
    while True:
        color = input('Introduce el color: ')
        if re.match('^[a-zA-Z]+$', color):
            return color
        else:
            print('El color debe ser una cadena de texto')

def velocidad():
    while True:
        try:
            velocidad = int(input('Introduce la velocidad: '))
            if velocidad < 0:
                print('La velocidad no puede ser negativa')
            else:
                return velocidad
        except ValueError:
            print('La velocidad debe ser un número entero')

def cilindrada():
    while True:
        try:
            cilindrada = int(input('Introduce la cilindrada: '))
            if cilindrada < 0:
                print('La cilindrada no puede ser negativa')
            else:
                return cilindrada
        except ValueError:
            print('La cilindrada debe ser un número entero')

def carga():
    while True:
        try:
            carga = int(input('Introduce la carga: '))
            if carga < 0:
                print('La carga no puede ser negativa')
            else:
                return carga
        except ValueError:
            print('La carga debe ser un número entero')

def tipo():
    while True:
        tipo = input('Introduce el tipo: ')
        if re.match('^[a-zA-Z]+$', tipo):
            return tipo
        else:
            print('El tipo debe ser una cadena de texto')

            
