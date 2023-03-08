import csv

class Ficheros:

    def agregar_evento(self):
        contenido = ["HOLA","hELLO"]
        with open("agenda.csv", "a",newline="") as archivo:
            escritor = csv.writer(archivo, delimiter=",")
            escritor.writerow(contenido)

hola = Ficheros()
hola.agregar_evento()