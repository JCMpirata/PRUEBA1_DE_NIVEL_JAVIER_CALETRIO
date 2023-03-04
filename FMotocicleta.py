import FBicicleta
import csv
import config

class Motocicleta(FBicicleta.Bicicleta):
    def __init__(self, codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada):
        super().__init__(codigo, marca, modelo, color, ruedas, precio, velocidad)
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f" {self.cilindrada}"

    def to_dict(self):
        return {**super().to_dict(), 'cilindrada': self.cilindrada}
    
class Motocicletas(FBicicleta.Bicicletas):
    
        lista = []
        for vehiculo in FBicicleta.Bicicletas.lista:
            if isinstance(vehiculo, Motocicleta):
                lista.append(vehiculo)
        
        @staticmethod
        def buscar(codigo):
            for vehiculo in Motocicletas.lista:
                if vehiculo.codigo == codigo:
                    return vehiculo
                
        @staticmethod
        def crear(codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada):
            vehiculo = Motocicleta(codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada)
            Motocicletas.lista.append(vehiculo)
            Motocicletas.guardar()
            return vehiculo
        
        @staticmethod
        def modificar(codigo, marca, modelo, color, ruedas, precio, velocidad, cilindrada):
            for indice, vehiculo in enumerate(Motocicletas.lista):
                if vehiculo.codigo == codigo:
                    Motocicletas.lista[indice].marca = marca
                    Motocicletas.lista[indice].modelo = modelo
                    Motocicletas.lista[indice].color = color
                    Motocicletas.lista[indice].ruedas = ruedas
                    Motocicletas.lista[indice].precio = precio
                    Motocicletas.lista[indice].velocidad = velocidad
                    Motocicletas.lista[indice].cilindrada = cilindrada
                    Motocicletas.guardar()
                    return Motocicletas.lista[indice]
                
        @staticmethod
        def borrar(codigo):
            for indice, vehiculo in enumerate(Motocicletas.lista):
                if vehiculo.codigo == codigo:
                    vehiculo = Motocicletas.lista.pop(indice)
                    Motocicletas.guardar()
                    return vehiculo
                
        @staticmethod
        def guardar():
            with open(config.DATABASE_PATH, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['codigo', 'marca', 'modelo', 'color', 'ruedas', 'precio', 'velocidad', 'cilindrada'])
                for vehiculo in Motocicletas.lista:
                    writer.writerow([vehiculo.codigo, vehiculo.marca, vehiculo.modelo, vehiculo.color, vehiculo.ruedas, vehiculo.precio, vehiculo.velocidad, vehiculo.cilindrada])