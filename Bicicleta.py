class Bicicleta():
    def __init__(self, color, ruedas, tipo):
        self.color = color
        self.ruedas = ruedas
        self.tipo = tipo
    def __str__(self):
        return "Color: %s, Ruedas: %s, Tipo: %s" % (self.color, self.ruedas, self.tipo)