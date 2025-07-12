from claseColectivo import Colectivo
import csv
import numpy as np
class ManejadorColectivo:
    __arreglo: np.ndarray
    __cantidad: int
    __dimension: int
    def __init__(self, dimension):
        self.__cantidad = 0
        self.__dimension = 4
        self.__arreglo = np.empty(4, dtype=Colectivo)
    def mostrar(self):
        for colectivo in self.__arreglo:
            colectivo.mostrar()
    def agregar(self, colectivo):
        if  self.__cantidad < self.__dimension:
            self.__arreglo[self.__cantidad] = colectivo
            self.__cantidad+=1
        else:
            print("no se puede agregar mas")
    def cargar(self):
        archivo = open("colectivos.csv")
        reader = csv.reader(archivo, delimiter=";")
        next(reader)
        for fila in reader:
            patente=str(fila[0])
            marca=str(fila[1])
            modelo=int(fila[2])
            capacidad=int(fila[3])
            dni=int(fila[4])
            self.agregar(Colectivo(patente, marca, modelo, capacidad, dni))
        archivo.close()
    def buscardni(self, pat):
        i = 0
        long = len(self.__arreglo)
        while i < long:
            if self.__arreglo[i].getpatentec()==pat:
                return self.__arreglo[i]
            i+=1
    def mostrarB(self, mt):
        i=0
        long = len(self.__arreglo)
        while i<long:
            km = mt.cantidadtotal(self.__arreglo[i].getpatentec()) 
            gasto = (km/100)*  self.__arreglo[i].getconsumo()
            print(f"Para el colectivo {i+1}")
            print(f"km recorridos: {km}, gasto estimado: {gasto}")
            i+=1
            