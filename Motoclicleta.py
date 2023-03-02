class Motoclicleta():
    def __init__(self, color, ruedas, velocidad, cilindrada):
        self.color = color
        self.ruedas = ruedas
        self.velocidad = velocidad
        self.cilindrada = cilindrada
    def __str__(self):
        return "Color: % Ruedas: % Velocidad: % Cilindrada: " % self.color, self.ruedas, self.velocidad, self.cilindrada