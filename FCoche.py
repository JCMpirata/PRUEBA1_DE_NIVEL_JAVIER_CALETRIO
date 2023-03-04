import BDVehiculo
import config
import csv

class Coche(BDVehiculo.Vehiculo):
    def __init__(self, modelo, marca, color, ruedas, precio, velocidad, cilindrada):
        super().__init__(modelo, marca, color, ruedas, precio)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f" {self.velocidad} {self.cilindrada}"

    def to_dict(self):
        return {**super().to_dict(), 'velocidad': self.velocidad, 'cilindrada': self.cilindrada}
    
class Coches(BDVehiculo.Vehiculos):

    lista = []
    for vehiculo in BDVehiculo.Vehiculos.lista:
        if isinstance(vehiculo, Coche):
            lista.append(vehiculo)
    
    @staticmethod
    def buscar(modelo):
        for vehiculo in Coches.lista:
            if vehiculo.modelo == modelo:
                return vehiculo
            
    @staticmethod
    def crear(modelo, marca, color, ruedas, precio, velocidad, cilindrada):
        vehiculo = Coche(modelo, marca, color, ruedas, precio, velocidad, cilindrada)
        Coches.lista.append(vehiculo)
        Coches.guardar()
        return vehiculo
    
    @staticmethod
    def modificar(modelo, marca, color, ruedas, precio, velocidad, cilindrada):
        for indice, vehiculo in enumerate(Coches.lista):
            if vehiculo.modelo == modelo:
                Coches.lista[indice].modelo = modelo
                Coches.lista[indice].marca = marca
                Coches.lista[indice].color = color
                Coches.lista[indice].ruedas = ruedas
                Coches.lista[indice].precio = precio
                Coches.lista[indice].velocidad = velocidad
                Coches.lista[indice].cilindrada = cilindrada
                Coches.guardar()
                return Coches.lista[indice]
            
    @staticmethod
    def borrar(modelo):
        for indice, vehiculo in enumerate(Coches.lista):
            if vehiculo.modelo == modelo:
                vehiculo = Coches.lista.pop(indice)
                Coches.guardar()
                return vehiculo
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Coches.lista:
                writer.writerow([vehiculo.modelo, vehiculo.marca, vehiculo.color, vehiculo.ruedas, vehiculo.precio, vehiculo.velocidad, vehiculo.cilindrada])


    
    