import BDVehiculo
import config
import csv

class Coche(BDVehiculo.Vehiculo):
    def __init__(self, codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada):
        super().__init__(codigo, marca, modelo, color, ruedas, precio)
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
    def buscar(codigo):
        for vehiculo in Coches.lista:
            if vehiculo.codigo == codigo:
                return vehiculo
            
    @staticmethod
    def crear(codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada):
        vehiculo = Coche(codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada)
        Coches.lista.append(vehiculo)
        Coches.guardar()
        return vehiculo
    
    @staticmethod
    def modificar(codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada):
        for indice, vehiculo in enumerate(Coches.lista):
            if vehiculo.codigo == codigo:
                Coches.lista[indice].marca = marca
                Coches.lista[indice].modelo = modelo
                Coches.lista[indice].color = color
                Coches.lista[indice].ruedas = ruedas
                Coches.lista[indice].precio = precio
                Coches.lista[indice].velocidad = velocidad
                Coches.lista[indice].cilindrada = cilindrada
                Coches.guardar()
                return Coches.lista[indice]
            
    @staticmethod
    def borrar(codigo):
        for indice, vehiculo in enumerate(Coches.lista):
            if vehiculo.codigo == codigo:
                vehiculo = Coches.lista.pop(indice)
                Coches.guardar()
                return vehiculo
            
    @staticmethod
    def guardar():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vehiculo in Coches.lista:
                writer.writerow(vehiculo.to_dict().values())


    
    