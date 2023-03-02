
class Camioneta():
    lista = []
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
        self.carga = carga
    def __str__(self):
        return "Color: %s, Ruedas: %s, Velocidad: %s, Cilindrada: %s, Carga: %s" % (self.color, self.ruedas, self.velocidad, self.cilindrada, self.carga)
    
