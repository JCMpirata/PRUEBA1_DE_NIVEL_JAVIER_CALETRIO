import FCoche
import config
import csv

class Furgoneta(FCoche.Coche):
    def __init__(self, modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, carga):
        super().__init__(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada)
        self.carga = carga

    def __str__(self):
        return super().__str__() + f" {self.carga}"

    def to_dict(self):
        return {**super().to_dict(), 'carga': self.carga}
    
class Furgonetas(FCoche.Coches):
    
        lista = []
        for vhc in FCoche.Coches.lista:
            if isinstance(vhc, Furgoneta):
                lista.append(vhc)
        
        @staticmethod
        def buscar_furgo(modelo):
            for vhc in Furgonetas.lista:
                if vhc.modelo == modelo:
                    return vhc
                
        @staticmethod
        def crear_furgo(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, carga):
            vhc = Furgoneta(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, carga)
            Furgonetas.lista.append(vhc)
            Furgonetas.guardar_furgo()
            return vhc
        
        @staticmethod
        def modificar_furgo(modelo, vehiculo, marca, color, ruedas, precio, velocidad, cilindrada, carga):
            for indice, vhc in enumerate(Furgonetas.lista):
                if vhc.modelo == modelo:
                    Furgonetas.lista[indice].modelo = modelo
                    Furgonetas.lista[indice].vehiculo = vehiculo
                    Furgonetas.lista[indice].marca = marca
                    Furgonetas.lista[indice].color = color
                    Furgonetas.lista[indice].ruedas = ruedas
                    Furgonetas.lista[indice].precio = precio
                    Furgonetas.lista[indice].velocidad = velocidad
                    Furgonetas.lista[indice].cilindrada = cilindrada
                    Furgonetas.lista[indice].carga = carga
                    Furgonetas.guardar_furgo()
                    return Furgonetas.lista[indice]
                
        @staticmethod
        def borrar_furgo(modelo):
            for indice, vhc in enumerate(Furgonetas.lista):
                if vhc.modelo == modelo:
                    vhc = Furgonetas.lista.pop(indice)
                    Furgonetas.guardar_furgo()
                    return vhc
                
        @staticmethod
        def guardar_furgo():
            with open(config.DATABASE_PATH, 'w') as fichero:
                writer = csv.writer(fichero, delimiter=';')
                for vhc in Furgonetas.lista:
                    writer.writerow([vhc.modelo, vhc.vehiculo, vhc.marca, vhc.color, vhc.ruedas, vhc.precio, vhc.velocidad, vhc.cilindrada, vhc.carga])

    
