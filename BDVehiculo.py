# Description: Clase que representa la tabla BDVehiculo de la base de datos

import csv
import config


class Vehiculo():
    def __init__(self, codigo, marca, modelo, ruedas: int, color, precio: float):
        self.codigo = codigo
        self.marca = marca
        self.modelo = modelo
        self.ruedas = ruedas
        self.color = color
        self.precio = precio

    def __str__(self):
        return f"({self.codigo}) {self.marca} {self.modelo} {self.ruedas} {self.color} {self.precio}"
    
    def to_dict(self):
        return {'codigo': self.codigo, 'marca': self.marca, 'modelo': self.modelo, 'ruedas': self.ruedas, 'color': self.color, 'precio': self.precio}
    
class Vehiculos():
    
    lista = []
    with open(config.DATABASE_PATH, newline='\n') as fichero:
        reader = csv.reader(fichero, delimiter=';')
        for codigo, marca, modelo, color, ruedas, precio in reader:
            vehiculo = Vehiculo(codigo, marca, modelo, color, ruedas, precio)
            lista.append(vehiculo)

    @staticmethod
    def buscar(codigo):
        for vehiculo in Vehiculos.lista:
            if vehiculo.codigo == codigo:
                return vehiculo
            
    @staticmethod
    def crear(codigo, marca, modelo, color, ruedas, precio):
        vehiculo = Vehiculo(codigo, marca, modelo, color, ruedas, precio)
        Vehiculos.lista.append(vehiculo)
        Vehiculos.guardar()
        return vehiculo
    
    @staticmethod
    def modificar(codigo, marca, modelo, color, ruedas, precio):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.codigo == codigo:
                Vehiculos.lista[indice].marca = marca
                Vehiculos.lista[indice].modelo = modelo
                Vehiculos.lista[indice].color = color
                Vehiculos.lista[indice].ruedas = ruedas
                Vehiculos.lista[indice].precio = precio
                Vehiculos.guardar()
                return Vehiculos.lista[indice]
            
    @staticmethod
    def borrar(codigo):
        for indice, vehiculo in enumerate(Vehiculos.lista):
            if vehiculo.codigo == codigo:
                vehiculo = Vehiculos.lista.pop(indice)
                Vehiculos.guardar()
                return vehiculo
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Vehiculos.lista:
                writer.writerow([vehiculo.codigo, vehiculo.marca, vehiculo.modelo, vehiculo.color, vehiculo.ruedas, vehiculo.precio])
                
    
    




    

