import config
import csv


class Vehiculo():
    def __init__(self, color, ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "Color: %s, Ruedas: %s" % (self.color, self.ruedas)
    
    def to_dict(self):
        return {'color': self.color, 'ruedas': self.ruedas}
    



    lista = []
    with open(config.DATABASE_PATH, "r") as f:
        reader = csv.reader









    
    

