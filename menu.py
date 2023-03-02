import os
import Vehiculo as vh
import helpers as hlp

def menu():
    while True:
        os.system('clear')
        print('1. Listar vehículos')
        print('2. Añadir vehículo')
        print('3. Eliminar vehículo')
        print('4. Salir')
        try:
            opcion = int(input('Introduce una opción: '))
            if opcion == 1:
                listar_vehiculos()
            elif opcion == 2:
                anadir_vehiculo()
            elif opcion == 3:
                eliminar_vehiculo()
            elif opcion == 4:
                break
            else:
                print('Opción incorrecta')
        except ValueError:
            print('Opción incorrecta')