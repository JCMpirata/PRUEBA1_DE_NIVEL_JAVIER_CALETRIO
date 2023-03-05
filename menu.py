import BDVehiculo as bdv
import FBicicleta as fbi
import FCoche as fco
import FFurgoneta as ffu
import FMotocicleta as fmo
import helpers as hlp

def iniciar_menu():
    while True:
        hlp.limpiar_pantalla()

        print("========================")
        print("  Bienvenido al Gestor de Vehiculos  ")
        print("========================")
        print("[1] Listar los vehiculos ")
        print("[2] Buscar un vehiculo   ")
        print("[3] Añadir un vehiculo   ")
        print("[4] Modificar un vehiculo")
        print("[5] Borrar un vehiculo   ")
        print("[6] Cerrar el Gestor    ")
        print("========================")

        opcion = input("Elija una opcion: ")

        if opcion == '1':
            print("Listando los vehiculos...\n")
            for vehiculo in bdv.Vehiculos.lista:
                print(vehiculo)

        elif opcion == '2':
            print("Buscando un vehiculo...\n")
            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
            vehiculo = bdv.Vehiculos.buscar(modelo)
            if modelo:
                print(vehiculo)
            else:
                print("Vehiculo no encontrado.")

        elif opcion == '3':
            print("Añadiendo un vehiculo...\n")

            modelo = None
            while True:
                modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
                if hlp.modelo_valido(modelo, bdv.Vehiculos.lista):
                    break

            vehiculo = hlp.leer_texto(2, 30, "Vehiculo (bicicleta, coche, motocicleta, furgoneta)").lower()
            marca = hlp.leer_texto(2, 30, "Marca (de 2 a 30 chars)").capitalize()
            color = hlp.leer_texto(2, 30, "Color (de 2 a 30 chars)").capitalize()
            precio = hlp.leer_entero(0, 1000000, "Precio (de 0 a 1000000 €)")
            tipo = hlp.leer_texto(2, 30, "Tipo (de 2 a 30 chars)").capitalize()
            velocidad = hlp.leer_entero(0, 300, "Velocidad (de 0 a 300 km/h)")
            cilindrada = hlp.leer_entero(0, 10000, "Cilindrada (de 0 a 10000 cc)")
            carga = hlp.leer_entero(0, 10000, "Carga (de 0 a 10000 kg)")

            ruedas = hlp.leer_entero(2 or 4, "Ruedas (2 o 4)")
            if hlp.ruedas_valido(ruedas):
                if ruedas == 2:
                    if vehiculo == "bicicleta":
                        fbi.Bicicletas.crear(modelo, marca, color, ruedas, precio, tipo)
                        print("Vehiculo añadido correctamente.")
                    elif vehiculo == "motocicleta":
                        fmo.Motocicletas.crear(modelo, marca, color, ruedas, precio, tipo, velocidad, cilindrada)
                        print("Vehiculo añadido correctamente.")
                    else:
                        print("Vehiculo no encontrado.")
                elif ruedas == 4:
                    if vehiculo == "coche":
                        fco.Coches.crear(modelo, marca, color, ruedas, precio, velocidad, cilindrada)
                        print("Vehiculo añadido correctamente.")
                    elif vehiculo == "furgoneta":
                        ffu.Furgonetas.crear(modelo, marca, color, ruedas, precio, velocidad, cilindrada, carga)
                        print("Vehiculo añadido correctamente.")
                    else:
                        print("Vehiculo no encontrado.")

        elif opcion == '4':
            print("Modificando un vehiculo...\n")
            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
            vehiculo = bdv.Vehiculos.buscar(modelo)
            if modelo:
                print(vehiculo)
                print("¿Desea modificar el vehiculo?")
                opcion = hlp.leer_texto(1, 1, "S/N").lower()
                if opcion == "s":
                    vehiculo.modificar()
                    print("Vehiculo modificado correctamente.")
                else:
                    print("Vehiculo no modificado.")
            else:
                print("Vehiculo no encontrado.")

        elif opcion == '5':
            print("Borrando un vehiculo...\n")
            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
            vehiculo = bdv.Vehiculos.buscar(modelo)
            if modelo:
                print(vehiculo)
                print("¿Desea borrar el vehiculo?")
                opcion = hlp.leer_texto(1, 1, "S/N").lower()
                if opcion == "s":
                    vehiculo.borrar()
                    print("Vehiculo borrado correctamente.")
                else:
                    print("Vehiculo no borrado.")
            else:
                print("Vehiculo no encontrado.")

        elif opcion == '6':
            print("Cerrando el Gestor...\n")
            break

        else:
            print("Opcion no valida.")

        input("Pulse ENTER para continuar...")

            
        





