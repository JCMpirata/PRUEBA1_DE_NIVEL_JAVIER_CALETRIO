import FCoche
import config
import csv

class Furgoneta(FCoche.Coche):
    def __init__(self, modelo, marca, color, ruedas, precio, velocidad, cilindrada, carga):
        super().__init__(modelo, marca, color, ruedas, precio, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f" {self.carga}"

    def to_dict(self):
        return {**super().to_dict(), 'carga': self.carga}
    
class Furgonetas(FCoche.Coches):
    
        lista = []
        for vehiculo in FCoche.Coches.lista:
            if isinstance(vehiculo, Furgoneta):
                lista.append(vehiculo)
        
        @staticmethod
        def buscar(modelo):
            for vehiculo in Furgonetas.lista:
                if vehiculo.modelo == modelo:
                    return vehiculo
                
        @staticmethod
        def crear(modelo, marca, color, ruedas, precio, velocidad, cilindrada, carga):
            vehiculo = Furgoneta(modelo, marca, color, ruedas, precio, velocidad, cilindrada, carga)
            Furgonetas.lista.append(vehiculo)
            Furgonetas.guardar()
            return vehiculo
        
        @staticmethod
        def modificar(modelo, marca, color, ruedas, precio, velocidad, cilindrada, carga):
            for indice, vehiculo in enumerate(Furgonetas.lista):
                if vehiculo.modelo == modelo:
                    Furgonetas.lista[indice].modelo = modelo
                    Furgonetas.lista[indice].marca = marca
                    Furgonetas.lista[indice].color = color
                    Furgonetas.lista[indice].ruedas = ruedas
                    Furgonetas.lista[indice].precio = precio
                    Furgonetas.lista[indice].velocidad = velocidad
                    Furgonetas.lista[indice].cilindrada = cilindrada
                    Furgonetas.lista[indice].carga = carga
                    Furgonetas.guardar()
                    return Furgonetas.lista[indice]
                
        @staticmethod
        def borrar(modelo):
            for indice, vehiculo in enumerate(Furgonetas.lista):
                if vehiculo.modelo == modelo:
                    vehiculo = Furgonetas.lista.pop(indice)
                    Furgonetas.guardar()
                    return vehiculo
                
        @staticmethod
        def guardar():
            with open(config.DATABASE_PATH, 'w') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for vehiculo in Furgonetas.lista:
                    writer.writerow([vehiculo.modelo, vehiculo.marca, vehiculo.color, vehiculo.ruedas, vehiculo.precio, vehiculo.velocidad, vehiculo.cilindrada, vehiculo.carga])

    
