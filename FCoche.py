import BDVehiculo
import config
import csv

class Coche(BDVehiculo.Vehiculo):
    def __init__(self, modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada):
        super().__init__(modelo, vehiculo, marca, color, ruedas, precio)
        self.velocidad = velocidad
        self.cilindrada = cilindrada

    def __str__(self):
        return super().__str__() + f" {self.velocidad} {self.cilindrada}"

    def to_dict(self):
        return {**super().to_dict(), 'velocidad': self.velocidad, 'cilindrada': self.cilindrada}
    
class Coches(BDVehiculo.Vehiculos):

    lista = []
    for vhc in BDVehiculo.Vehiculos.lista:
        if isinstance(vhc, Coche):
            lista.append(vhc)
    
    @staticmethod
    def buscar_coche(modelo):
        for vhc in Coches.lista:
            if vhc.modelo == modelo:
                return vhc
            
    @staticmethod
    def crear_coche(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada):
        vhc = Coche(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada)
        Coches.lista.append(vhc)
        Coches.guardar_coche()
        return vhc
    
    @staticmethod
    def modificar_coche(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada):
        for indice, vhc in enumerate(Coches.lista):
            if vhc.modelo == modelo:
                Coches.lista[indice].modelo = modelo
                Coches.lista[indice].vehiculo = vehiculo
                Coches.lista[indice].marca = marca
                Coches.lista[indice].color = color
                Coches.lista[indice].ruedas = ruedas
                Coches.lista[indice].precio = precio
                Coches.lista[indice].velocidad = velocidad
                Coches.lista[indice].cilindrada = cilindrada
                Coches.guardar_coche()
                return Coches.lista[indice]
            
    @staticmethod
    def borrar_coche(modelo):
        for indice, vhc in enumerate(Coches.lista):
            if vhc.modelo == modelo:
                vhc = Coches.lista.pop(indice)
                Coches.guardar_coche()
                return vhc
            
    @staticmethod
    def guardar_coche():
        with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
            writer = csv.writer(fichero, delimiter=';')
            for vhc in Coches.lista:
                writer.writerow([vhc.modelo, vhc.vehiculo, vhc.marca, vhc.color, vhc.ruedas, vhc.precio, vhc.velocidad, vhc.cilindrada])


    
    