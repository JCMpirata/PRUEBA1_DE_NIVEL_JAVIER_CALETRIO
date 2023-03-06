import BDVehiculo as bdv
import FBicicleta as fbi
import FCoche as fco
import FFurgoneta as ffu
import FQuad as fqu
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
        hlp.limpiar_pantalla()



        if opcion == '1':
            print("Listando los vehiculos...\n")
            for vhc in bdv.Vehiculos.lista:
                print(vhc)



        elif opcion == '2':
            print("Buscando un vehiculo...\n")
            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
            vhc = bdv.Vehiculos.buscar(modelo)
            if modelo:
                print(vhc)
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
            if hlp.ruedas_valido(ruedas) and hlp.vehiculo_valido(vehiculo):
                if ruedas == 2:
                    if vehiculo == "bicicleta":
                        fbi.Bicicletas.crear_bici(modelo, vehiculo, marca, color, ruedas, precio, tipo)
                        print("Vehiculo añadido correctamente.")
                    elif vehiculo == "motocicleta":
                        fmo.Motocicletas.crear_moto(modelo, vehiculo, marca, color, ruedas, precio, tipo, velocidad, cilindrada)
                        print("Vehiculo añadido correctamente.")
                    else:
                        print("Vehiculo no encontrado.")
                elif ruedas == 4:
                    if vehiculo == "coche":
                        fco.Coches.crear_coche(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada)
                        print("Vehiculo añadido correctamente.")
                    elif vehiculo == "furgoneta":
                        ffu.Furgonetas.crear_furgo(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, carga)
                        print("Vehiculo añadido correctamente.")
                    elif vehiculo == "quad":
                        fqu.Quads.crear_quad(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, carga)
                        print("Vehiculo añadido correctamente.")
                    else:
                        print("Vehiculo no encontrado.")
            else:
                print("Vehiculo no encontrado.")



        elif opcion == '4':
            print("Modificando un vehiculo...\n")
            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
            vhc = bdv.Vehiculos.buscar(modelo)
            if modelo:
                print(vhc)
                print("¿Desea modificar el vehiculo?")
                opcion = hlp.leer_texto(1, 1, "S/N").lower()
                if opcion == "s":
                    if vhc.ruedas == 2:
                        if vhc.vehiculo == "bicicleta":
                            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
                            vehiculo = hlp.leer_texto(2, 30, "Vehiculo (bicicleta, motocicleta)").lower()
                            marca = hlp.leer_texto(2, 30, "Marca (de 2 a 30 chars)").capitalize()
                            color = hlp.leer_texto(2, 30, "Color (de 2 a 30 chars)").capitalize()
                            ruedas = hlp.leer_entero(2 or 4, "Ruedas (2 o 4)")
                            precio = hlp.leer_entero(0, 1000000, "Precio (de 0 a 1000000 €)")
                            tipo = hlp.leer_texto(2, 30, "Tipo (de 2 a 30 chars)").capitalize()

                            fbi.Bicicletas.modificar_bici(modelo, vehiculo, marca, color, ruedas, precio, tipo)
                            print("Vehiculo modificado correctamente.")
                        
                        elif vhc.vehiculo == "motocicleta":
                            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
                            vehiculo = hlp.leer_texto(2, 30, "Vehiculo (bicicleta, motocicleta)").lower()
                            marca = hlp.leer_texto(2, 30, "Marca (de 2 a 30 chars)").capitalize()
                            color = hlp.leer_texto(2, 30, "Color (de 2 a 30 chars)").capitalize()
                            ruedas = hlp.leer_entero(2 or 4, "Ruedas (2 o 4)")
                            precio = hlp.leer_entero(0, 1000000, "Precio (de 0 a 1000000 €)")
                            tipo = hlp.leer_texto(2, 30, "Tipo (de 2 a 30 chars)").capitalize()
                            velocidad = hlp.leer_entero(0, 300, "Velocidad (de 0 a 300 km/h)")
                            cilindrada = hlp.leer_entero(0, 10000, "Cilindrada (de 0 a 10000 cc)")

                            fmo.Motocicletas.modificar_moto(modelo, vehiculo, marca, color, ruedas, precio, tipo, velocidad, cilindrada)
                            print("Vehiculo modificado correctamente.")
                        else:
                            print("Vehiculo no encontrado.")

                    elif vhc.ruedas == 4:
                        if vhc.vehiculo == "coche":
                            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
                            vehiculo = hlp.leer_texto(2, 30, "Vehiculo (coche, furgoneta, quad)").lower()
                            marca = hlp.leer_texto(2, 30, "Marca (de 2 a 30 chars)").capitalize()
                            color = hlp.leer_texto(2, 30, "Color (de 2 a 30 chars)").capitalize()
                            ruedas = hlp.leer_entero(2 or 4, "Ruedas (2 o 4)")
                            precio = hlp.leer_entero(0, 1000000, "Precio (de 0 a 1000000 €)")
                            velocidad = hlp.leer_entero(0, 300, "Velocidad (de 0 a 300 km/h)")
                            cilindrada = hlp.leer_entero(0, 10000, "Cilindrada (de 0 a 10000 cc)")

                            fco.Coches.modificar_coche(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada)
                            print("Vehiculo modificado correctamente.")

                        elif vhc.vehiculo == "furgoneta":
                            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
                            vehiculo = hlp.leer_texto(2, 30, "Vehiculo (coche, furgoneta, quad)").lower()
                            marca = hlp.leer_texto(2, 30, "Marca (de 2 a 30 chars)").capitalize()
                            color = hlp.leer_texto(2, 30, "Color (de 2 a 30 chars)").capitalize()
                            ruedas = hlp.leer_entero(2 or 4, "Ruedas (2 o 4)")
                            precio = hlp.leer_entero(0, 1000000, "Precio (de 0 a 1000000 €)")
                            velocidad = hlp.leer_entero(0, 300, "Velocidad (de 0 a 300 km/h)")
                            cilindrada = hlp.leer_entero(0, 10000, "Cilindrada (de 0 a 10000 cc)")
                            carga = hlp.leer_entero(0, 10000, "Carga (de 0 a 10000 kg)")

                            ffu.Furgonetas.modificar_furgo(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, carga)
                            print("Vehiculo modificado correctamente.")

                        elif vhc.vehiculo == "quad":
                            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
                            vehiculo = hlp.leer_texto(2, 30, "Vehiculo (coche, furgoneta, quad)").lower()
                            marca = hlp.leer_texto(2, 30, "Marca (de 2 a 30 chars)").capitalize()
                            color = hlp.leer_texto(2, 30, "Color (de 2 a 30 chars)").capitalize()
                            ruedas = hlp.leer_entero(2 or 4, "Ruedas (2 o 4)")
                            precio = hlp.leer_entero(0, 1000000, "Precio (de 0 a 1000000 €)")
                            velocidad = hlp.leer_entero(0, 300, "Velocidad (de 0 a 300 km/h)")
                            cilindrada = hlp.leer_entero(0, 10000, "Cilindrada (de 0 a 10000 cc)")
                            tipo = hlp.leer_texto(2, 30, "Tipo (de 2 a 30 chars)").capitalize()
                            carga = hlp.leer_entero(0, 10000, "Carga (de 0 a 10000 kg)")

                            fqu.Quads.modificar_quad(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, tipo, carga)
                            print("Vehiculo modificado correctamente.")
                        else:
                            print("Vehiculo no encontrado.")
                    else:
                        print("Vehiculo no modificado.")
                else:
                    print("Vehiculo no encontrado.")



        elif opcion == '5':
            print("Borrando un vehiculo...\n")
            modelo = hlp.leer_texto(2, 30, "Modelo (de 2 a 30 chars)").capitalize()
            vhc = bdv.Vehiculos.buscar(modelo)
            if modelo:
                print(vhc)
                print("¿Desea borrar el vehiculo?")
                opcion = hlp.leer_texto(1, 1, "S/N").lower()
                if opcion == "s":
                    if vhc.ruedas == 2:
                        if vhc.vehiculo == "bicicleta":
                            fbi.Bicicletas.borrar_bici(vhc)
                            print("Vehiculo borrado correctamente.")
                        elif vhc.vehiculo == "motocicleta":
                            fmo.Motocicletas.borrar_moto(vhc)
                            print("Vehiculo borrado correctamente.")
                        else:
                            print("Vehiculo no encontrado.")
                    elif vhc.ruedas == 4:
                        if vhc.vehiculo == "coche":
                            fco.Coches.borrar_coche(vhc)
                            print("Vehiculo borrado correctamente.")
                        elif vhc.vehiculo == "furgoneta":
                            ffu.Furgonetas.borrar_furgo(vhc)
                            print("Vehiculo borrado correctamente.")
                        else:
                            print("Vehiculo no encontrado.")
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

            
        





