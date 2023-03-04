import BDVehiculo
import config
import csv

class Bicicleta(BDVehiculo.Vehiculo):

    def __init__(self, modelo, marca, color, ruedas, precio, tipo):
        super().__init__(modelo, marca, color, ruedas, precio)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f" {self.tipo}"

    def to_dict(self):
        return {**super().to_dict(), 'velocidad': self.tipo}
    
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
        def crear(modelo, marca, color, ruedas, precio, tipo):
            vehiculo = Bicicleta(modelo, marca, modelo, color, ruedas, precio, tipo)
            Bicicletas.lista.append(vehiculo)
            Bicicletas.guardar()
            return vehiculo
        
        @staticmethod
        def modificar(modelo, marca, color, ruedas, precio, tipo):
            for indice, vehiculo in enumerate(Bicicletas.lista):
                if vehiculo.modelo == modelo:
                    Bicicletas.lista[indice].modelo = modelo
                    Bicicletas.lista[indice].marca = marca
                    Bicicletas.lista[indice].color = color
                    Bicicletas.lista[indice].ruedas = ruedas
                    Bicicletas.lista[indice].precio = precio
                    Bicicletas.lista[indice].tipo = tipo
                    Bicicletas.guardar()
                    return Bicicletas.lista[indice]
                
        @staticmethod
        def borrar(modelo):
            for indice, vehiculo in enumerate(Bicicletas.lista):
                if vehiculo.modelo == modelo:
                    vehiculo = Bicicletas.lista.pop(indice)
                    Bicicletas.guardar()
                    return vehiculo
                
        @staticmethod
        def guardar():
            with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for vehiculo in Bicicletas.lista:
                    writer.writerow([vehiculo.modelo, vehiculo.marca, vehiculo.color, vehiculo.ruedas, vehiculo.precio, vehiculo.tipo])