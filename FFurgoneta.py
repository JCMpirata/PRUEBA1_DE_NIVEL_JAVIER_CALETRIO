import FCoche
import config
import csv

class Furgoneta(FCoche.Coche):
    def __init__(self, codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada, carga):
        super().__init__(codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada)
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
        def buscar(codigo):
            for vehiculo in Furgonetas.lista:
                if vehiculo.codigo == codigo:
                    return vehiculo
                
        @staticmethod
        def crear(codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada, carga):
            vehiculo = Furgoneta(codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada, carga)
            Furgonetas.lista.append(vehiculo)
            Furgonetas.guardar()
            return vehiculo
        
        @staticmethod
        def modificar(codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada, carga):
            for indice, vehiculo in enumerate(Furgonetas.lista):
                if vehiculo.codigo == codigo:
                    Furgonetas.lista[indice].marca = marca
                    Furgonetas.lista[indice].modelo = modelo
                    Furgonetas.lista[indice].color = color
                    Furgonetas.lista[indice].ruedas = ruedas
                    Furgonetas.lista[indice].precio = precio
                    Furgonetas.lista[indice].velocidad = velocidad
                    Furgonetas.lista[indice].cilindrada = cilindrada
                    Furgonetas.lista[indice].carga = carga
                    Furgonetas.guardar()
                    return Furgonetas.lista[indice]
                
        @staticmethod
        def borrar(codigo):
            for indice, vehiculo in enumerate(Furgonetas.lista):
                if vehiculo.codigo == codigo:
                    vehiculo = Furgonetas.lista.pop(indice)
                    Furgonetas.guardar()
                    return vehiculo
                
        @staticmethod
        def guardar():
            with open(config.DATABASE_PATH, 'w') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for vehiculo in Furgonetas.lista:
                    writer.writerow(vehiculo.to_dict().values())

    
