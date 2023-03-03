import BDVehiculo
import config
import csv

class Bicicleta(BDVehiculo.Vehiculo):

    def __init__(self, codigo, marca, modelo, color, ruedas, precio, velocidad, plato, piñon):
        super().__init__(codigo, marca, modelo, color, ruedas, precio)
        self.velocidad = velocidad
        self.plato = plato
        self.piñon = piñon

    def __str__(self):
        return super().__str__() + f" {self.velocidad} {self.plato} {self.piñon}"

    def to_dict(self):
        return {**super().to_dict(), 'velocidad': self.velocidad, 'plato': self.plato, 'piñon': self.piñon}