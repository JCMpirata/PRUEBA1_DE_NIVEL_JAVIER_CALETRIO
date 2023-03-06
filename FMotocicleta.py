import FBicicleta
import csv
import config

class Motocicleta(FBicicleta.Bicicleta):
    def __init__(self, modelo, vehiculo, marca, color, ruedas, precio, tipo, velocidad, cilindrada):
        super().__init__(modelo, vehiculo, marca, color, ruedas, precio, tipo)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f" {self.velocidad} {self.cilindrada}"

    def to_dict(self):
        return {**super().to_dict(), 'velocidad': self.velocidad, 'cilindrada': self.cilindrada}
    
class Motocicletas(FBicicleta.Bicicletas):
    
        lista = []
        for vhc in FBicicleta.Bicicletas.lista:
            if isinstance(vhc, Motocicleta):
                lista.append(vhc)
        
        @staticmethod
        def buscar_moto(modelo):
            for vhc in Motocicletas.lista:
                if vhc.modelo == modelo:
                    return vhc
                
        @staticmethod
        def crear_moto(modelo, vehiculo, marca, color, ruedas, precio, tipo, velocidad, cilindrada):
            vhc = Motocicleta(modelo, vehiculo, marca, color, ruedas, precio, tipo, velocidad, cilindrada)
            Motocicletas.lista.append(vhc)
            Motocicletas.guardar_moto()
            return vhc
        
        @staticmethod
        def modificar_moto(modelo, vehiculo, marca, color, ruedas, precio, tipo, velocidad, cilindrada):
            for indice, vhc in enumerate(Motocicletas.lista):
                if vhc.modelo == modelo:
                    Motocicletas.lista[indice].modelo = modelo
                    Motocicletas.lista[indice].vehiculo = vehiculo
                    Motocicletas.lista[indice].marca = marca
                    Motocicletas.lista[indice].color = color
                    Motocicletas.lista[indice].ruedas = ruedas
                    Motocicletas.lista[indice].precio = precio
                    Motocicletas.lista[indice].tipo = tipo
                    Motocicletas.lista[indice].velocidad = velocidad
                    Motocicletas.lista[indice].cilindrada = cilindrada
                    Motocicletas.guardar_moto()
                    return Motocicletas.lista[indice]
                
        @staticmethod
        def borrar_moto(modelo):
            for indice, vhc in enumerate(Motocicletas.lista):
                if vhc.modelo == modelo:
                    vhc = Motocicletas.lista.pop(indice)
                    Motocicletas.guardar_moto()
                    return vhc
                
        @staticmethod
        def guardar_moto():
            with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for vhc in Motocicletas.lista:
                    writer.writerow([vhc.modelo, vhc.vehiculo, vhc.marca, vhc.color, vhc.ruedas, vhc.precio, vhc.tipo, vhc.velocidad, vhc.cilindrada])