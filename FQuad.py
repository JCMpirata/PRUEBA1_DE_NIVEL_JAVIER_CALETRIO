import FCoche
import FBicicleta
import config
import csv

class Quad(FCoche.Coche, FBicicleta.Bicicleta):
    def __init__(self, modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, tipo, carga):
        super().__init__(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada)
        self.tipo = tipo
        self.carga = carga

    def __str__(self):
        return super().__str__() + f" {self.tipo} {self.carga}"

    def to_dict(self):
        return {**super().to_dict(), 'tipo': self.tipo, 'carga': self.carga}
    
class Quads(FCoche.Coches, FBicicleta.Bicicletas):
    
        lista = []
        for vhc in FCoche.Coches.lista:
            if isinstance(vhc, Quad):
                lista.append(vhc)
        for vhc in FBicicleta.Bicicletas.lista:
            if isinstance(vhc, Quad):
                lista.append(vhc)

        
        @staticmethod
        def buscar_quad(modelo):
            for vhc in Quads.lista:
                if vhc.modelo == modelo:
                    return vhc
                
        @staticmethod
        def crear_quad(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, tipo, carga):
            vhc = Quad(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, tipo, carga)
            Quads.lista.append(vhc)
            Quads.guardar_quad()
            return vhc
        
        @staticmethod
        def modificar_quad(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, tipo, carga):
            for indice, vhc in enumerate(Quads.lista):
                if vhc.modelo == modelo:
                    Quads.lista[indice].modelo = modelo
                    Quads.lista[indice].vehiculo = vehiculo
                    Quads.lista[indice].marca = marca
                    Quads.lista[indice].color = color
                    Quads.lista[indice].ruedas = ruedas
                    Quads.lista[indice].precio = precio
                    Quads.lista[indice].velocidad = velocidad
                    Quads.lista[indice].cilindrada = cilindrada
                    Quads.lista[indice].tipo = tipo
                    Quads.lista[indice].carga = carga
                    Quads.guardar_quad()
                    return Quads.lista[indice]
                
        @staticmethod
        def borrar_quad(modelo):
            for indice, vhc in enumerate(Quads.lista):
                if vhc.modelo == modelo:
                    vhc = Quads.lista.pop(indice)
                    Quads.guardar_quad()
                    return vhc
                
        @staticmethod
        def guardar_quad():
            with open(config.DATABASE_PATH, 'w', newline='\n') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for vhc in Quads.lista:
                    writer.writerow([vhc.modelo, vhc.vehiculo, vhc.marca, vhc.color, vhc.ruedas, vhc.precio, vhc.velocidad, vhc.cilindrada, vhc.tipo, vhc.carga])