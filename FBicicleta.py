import BDVehiculo
import config
import csv

class Bicicleta(BDVehiculo.Vehiculo):

    def __init__(self, codigo, marca, modelo, color, ruedas, precio, velocidad):
        super().__init__(codigo, marca, modelo, color, ruedas, precio)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__() + f" {self.velocidad}"

    def to_dict(self):
        return {**super().to_dict(), 'velocidad': self.velocidad}
    
class Bicicletas(BDVehiculo.Vehiculos):
    
        lista = []
        for vehiculo in BDVehiculo.Vehiculos.lista:
            if isinstance(vehiculo, Bicicleta):
                lista.append(vehiculo)
        
        @staticmethod
        def buscar(codigo):
            for vehiculo in Bicicletas.lista:
                if vehiculo.codigo == codigo:
                    return vehiculo
                
        @staticmethod
        def crear(codigo, marca, modelo, color, ruedas, precio, velocidad):
            vehiculo = Bicicleta(codigo, marca, modelo, color, ruedas, precio, velocidad)
            Bicicletas.lista.append(vehiculo)
            Bicicletas.guardar()
            return vehiculo
        
        @staticmethod
        def modificar(codigo, marca, modelo, color, ruedas, precio, velocidad):
            for indice, vehiculo in enumerate(Bicicletas.lista):
                if vehiculo.codigo == codigo:
                    Bicicletas.lista[indice].marca = marca
                    Bicicletas.lista[indice].modelo = modelo
                    Bicicletas.lista[indice].color = color
                    Bicicletas.lista[indice].ruedas = ruedas
                    Bicicletas.lista[indice].precio = precio
                    Bicicletas.lista[indice].velocidad = velocidad
                    Bicicletas.guardar()
                    return Bicicletas.lista[indice]
                
        @staticmethod
        def borrar(codigo):
            for indice, vehiculo in enumerate(Bicicletas.lista):
                if vehiculo.codigo == codigo:
                    vehiculo = Bicicletas.lista.pop(indice)
                    Bicicletas.guardar()
                    return vehiculo
                
        @staticmethod
        def guardar():
            with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for vehiculo in Bicicletas.lista:
                    writer.writerow(vehiculo.to_dict().values())