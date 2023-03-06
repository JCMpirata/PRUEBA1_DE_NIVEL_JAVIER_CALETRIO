# Description: Clase que representa la tabla BDVehiculo de la base de datos

import csv
import config


class Vehiculo():
    def __init__(self, modelo, vehiculo, marca, ruedas: int, color, precio: float):
        self.modelo = modelo
        self.vehiculo = vehiculo
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.precio = precio

    def __str__(self):
        return f"({self.modelo}) {self.vehiculo} {self.marca} {self.ruedas} {self.color} {self.precio}"
    
    def to_dict(self):
        return {'modelo': self.modelo, 'vehiculo': self.vehiculo, 'marca': self.marca, 'ruedas': self.ruedas, 'color': self.color, 'precio': self.precio}
    
class Vehiculos():
    
    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for modelo, vehiculo, marca, color, ruedas, precio in reader:
            vhc = Vehiculo(modelo, vehiculo, marca, color, ruedas, precio)
            lista.append(vhc)

    @staticmethod
    def buscar(modelo):
        for vhc in Vehiculos.lista:
            if vhc.modelo == modelo:
                return vhc
            
    @staticmethod
    def crear(modelo, vehiculo, marca, color, ruedas, precio):
        vhc = Vehiculo(modelo, vehiculo, marca, color, ruedas, precio)
        Vehiculos.lista.append(vhc)
        Vehiculos.guardar()
        return vhc
    
    @staticmethod
    def modificar(modelo, vehiculo, marca, color, ruedas, precio):
        for indice, vhc in enumerate(Vehiculos.lista):
            if vhc.modelo == modelo:
                Vehiculos.lista[indice].marca = marca
                Vehiculos.lista[indice].vehiculo = vehiculo
                Vehiculos.lista[indice].color = color
                Vehiculos.lista[indice].ruedas = ruedas
                Vehiculos.lista[indice].precio = precio
                Vehiculos.guardar()
                return Vehiculos.lista[indice]
            
    @staticmethod
    def borrar(modelo):
        for indice, vhc in enumerate(Vehiculos.lista):
            if vhc.modelo == modelo:
                vhc = Vehiculos.lista.pop(indice)
                Vehiculos.guardar()
                return vhc
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vhc in Vehiculos.lista:
                writer.writerow([vhc.modelo, vhc.vehiculo, vhc.marca, vhc.color, vhc.ruedas, vhc.precio])
                
    
    




    


