import config
import csv
import Coche
import Camioneta
import Motocicleta
import Bicicleta


class Vehiculo():

    lista = []
    with open(config.DATABASE_PATH, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == "Coche":
                lista.append(Coche.Coche(row[1], row[2], row[3], row[4]))
            if row[0] == "Camioneta":
                lista.append(Camioneta.Camioneta(row[1], row[2], row[3], row[4], row[5]))
            if row[0] == "Motocicleta":
                lista.append(Motocicleta.Motoclicleta(row[1], row[2], row[3], row[4]))
            if row[0] == "Bicicleta":
                lista.append(Bicicleta.Bicicleta(row[1], row[2], row[3]))
    
    




    

