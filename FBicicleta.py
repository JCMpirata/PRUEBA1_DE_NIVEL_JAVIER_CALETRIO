import BDVehiculo
import config
import csv

class Bicicleta(BDVehiculo.Vehiculo):

    def __init__(self, modelo, vehiculo, marca, color, ruedas, precio, tipo):
        super().__init__(modelo, vehiculo, marca, color, ruedas, precio)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f" {self.tipo}"

    def to_dict(self):
        return {**super().to_dict(), 'velocidad': self.tipo}
    
class Bicicletas(BDVehiculo.Vehiculos):
    
        lista = []
        for vhc in BDVehiculo.Vehiculos.lista:
            if isinstance(vhc, Bicicleta):
                lista.append(vhc)
        
        @staticmethod
        def buscar_bici(modelo):
            for vhc in Bicicletas.lista:
                if vhc.modelo == modelo:
                    return modelo
                
        @staticmethod
        def crear_bici(modelo, vehiculo, marca, color, ruedas, precio, tipo):
            vhc = Bicicleta(modelo, vehiculo, marca, modelo, color, ruedas, precio, tipo)
            Bicicletas.lista.append(vhc)
            Bicicletas.guardar_bici()
            return vhc
        
        @staticmethod
        def modificar_bici(modelo, vehiculo, marca, color, ruedas, precio, tipo):
            for indice, vhc in enumerate(Bicicletas.lista):
                if vhc.modelo == modelo:
                    Bicicletas.lista[indice].modelo = modelo
                    Bicicletas.lista[indice].vehiculo = vehiculo
                    Bicicletas.lista[indice].marca = marca
                    Bicicletas.lista[indice].color = color
                    Bicicletas.lista[indice].ruedas = ruedas
                    Bicicletas.lista[indice].precio = precio
                    Bicicletas.lista[indice].tipo = tipo
                    Bicicletas.guardar_bici()
                    return Bicicletas.lista[indice]
                
        @staticmethod
        def borrar_bici(modelo):
            for indice, vhc in enumerate(Bicicletas.lista):
                if vhc.modelo == modelo:
                    vhc = Bicicletas.lista.pop(indice)
                    Bicicletas.guardar_bici()
                    return vhc
                
        @staticmethod
        def guardar_bici():
            with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for vhc in Bicicletas.lista:
                    writer.writerow([vhc.modelo, vhc.vehiculo, vhc.marca, vhc.color, vhc.ruedas, vhc.precio, vhc.tipo])