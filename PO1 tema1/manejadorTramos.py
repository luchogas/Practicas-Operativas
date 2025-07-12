from claseTramo import Tramo
import csv

class manejadorTramo:
    __lista = []
    def __init__(self):
        self.__lista = []

    def mostrar(self):
        for tramo in self.__lista:
            tramo.mostrar()
    def cargar(self):
        archivo = open("tramos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            origen = str(fila[0])
            destino = str(fila[1])
            distancia = int(fila[2])
            patente = str(fila[3])
            self.__lista.append(Tramo(origen, destino, distancia, patente))
        archivo.close()

    def listado(self, dni, mc):
        total  = 0
        i=0
        long = len(self.__lista)
        while i < long:
            pat = mc.buscardni(self.__lista[i].getpatente())
            if pat.getdni() == dni:
                print(f"Origen: {self.__lista[i].getorigen()}, Destino: {self.__lista[i].getdestino()}, Km: {self.__lista[i].getdistancia()}")
                total += self.__lista[i].getdistancia()
            i += 1
        print(f"Total Km recorridos: {total}")
            
    def cantidadtotal(self,patente):
        acum=0
        for i in range(len(self.__lista)):
            if self.__lista[i].getpatente()==patente:
                acum+=self.__lista[i].getdistancia()
        return acum
    def tramosmayores(self, distancia):
        for i in range(len(self.__lista)):
            if self.__lista[i].getdistancia() > distancia:
                print(f"Origen: {self.__lista[i].getorigen()}, Destino: {self.__lista[i].getdestino()}, Distancia: {self.__lista[i].getdistancia()}")
