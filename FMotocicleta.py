import FBicicleta
import csv
import config

class Motocicleta(FBicicleta.Bicicleta):
    def __init__(self, modelo, marca, color, ruedas, precio, tipo, velocidad, cilindrada):
        super().__init__(modelo, marca, color, ruedas, precio, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f" {self.velocidad} {self.cilindrada}"

    def to_dict(self):
        return {**super().to_dict(), 'velocidad': self.velocidad, 'cilindrada': self.cilindrada}
    
class Motocicletas(FBicicleta.Bicicletas):
    
        lista = []
        for vehiculo in FBicicleta.Bicicletas.lista:
            if isinstance(vehiculo, Motocicleta):
                lista.append(vehiculo)
        
        @staticmethod
        def buscar(modelo):
            for vehiculo in Motocicletas.lista:
                if vehiculo.modelo == modelo:
                    return vehiculo
                
        @staticmethod
        def crear(modelo, marca, color, ruedas, precio, tipo, velocidad, cilindrada):
            vehiculo = Motocicleta(modelo, marca, color, ruedas, precio, tipo, velocidad, cilindrada)
            Motocicletas.lista.append(vehiculo)
            Motocicletas.guardar()
            return vehiculo
        
        @staticmethod
        def modificar(modelo, marca, color, ruedas, precio, tipo, velocidad, cilindrada):
            for indice, vehiculo in enumerate(Motocicletas.lista):
                if vehiculo.modelo == modelo:
                    Motocicletas.lista[indice].modelo = modelo
                    Motocicletas.lista[indice].marca = marca
                    Motocicletas.lista[indice].color = color
                    Motocicletas.lista[indice].ruedas = ruedas
                    Motocicletas.lista[indice].precio = precio
                    Motocicletas.lista[indice].tipo = tipo
                    Motocicletas.lista[indice].velocidad = velocidad
                    Motocicletas.lista[indice].cilindrada = cilindrada
                    Motocicletas.guardar()
                    return Motocicletas.lista[indice]
                
        @staticmethod
        def borrar(modelo):
            for indice, vehiculo in enumerate(Motocicletas.lista):
                if vehiculo.modelo == modelo:
                    vehiculo = Motocicletas.lista.pop(indice)
                    Motocicletas.guardar()
                    return vehiculo
                
        @staticmethod
        def guardar():
            with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for vehiculo in Motocicletas.lista:
                    writer.writerow([vehiculo.modelo, vehiculo.marca, vehiculo.color, vehiculo.ruedas, vehiculo.precio, vehiculo.tipo, vehiculo.velocidad, vehiculo.cilindrada])