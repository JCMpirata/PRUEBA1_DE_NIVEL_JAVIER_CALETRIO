# Description: Clase que representa la tabla BDVehiculo de la base de datos

import csv
import config


class Vehiculo():
    def __init__(self, modelo, marca, ruedas: int, color, precio: float):
        self.modelo = modelo
        self.marca = marca
        self.ruedas = ruedas
        self.color = color
        self.precio = precio

    def __str__(self):
        return f"({self.modelo}) {self.marca} {self.ruedas} {self.color} {self.precio}"
    
    def to_dict(self):
        return {'modelo': self.modelo, 'marca': self.marca, 'ruedas': self.ruedas, 'color': self.color, 'precio': self.precio}
    
class Vehiculos():
    
    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for modelo, marca, color, ruedas, precio in reader:
            vehiculo = Vehiculo(modelo, marca, color, ruedas, precio)
            lista.append(vehiculo)

    @staticmethod
    def buscar(modelo):
        for vehiculo in Vehiculos.lista:
            if vehiculo.modelo == modelo:
                return vehiculo
            
    @staticmethod
    def crear(modelo, marca, color, ruedas, precio):
        vehiculo = Vehiculo(modelo, marca, color, ruedas, precio)
        Vehiculos.lista.append(vehiculo)
        Vehiculos.guardar()
        return vehiculo
    
    @staticmethod
    def modificar(modelo, marca, color, ruedas, precio):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.modelo == modelo:
                Vehiculos.lista[indice].marca = marca
                Vehiculos.lista[indice].color = color
                Vehiculos.lista[indice].ruedas = ruedas
                Vehiculos.lista[indice].precio = precio
                Vehiculos.guardar()
                return Vehiculos.lista[indice]
            
    @staticmethod
    def borrar(modelo):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.modelo == modelo:
                vehiculo = Vehiculos.lista.pop(indice)
                Vehiculos.guardar()
                return vehiculo
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Vehiculos.lista:
                writer.writerow([vehiculo.modelo, vehiculo.marca, vehiculo.color, vehiculo.ruedas, vehiculo.precio])
                
    
    




    

