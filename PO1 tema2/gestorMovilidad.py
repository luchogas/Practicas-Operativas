from claseMovilidad import Movilidad
import csv
import numpy as np
class GestorMovilidad:
    __arreglo = np.ndarray
    __cantidad = int
    __dimension = int
    def __init__(self):
        self.__dimension = 4
        self.__cantidad = 0
        self.__arreglo = np.empty(4, dtype=Movilidad)

    def mostrar(self):
        for movilidad in self.__arreglo:
            movilidad.mostrar()
    def agregar(self, movilidad):
        if self.__cantidad < self.__dimension:
            self.__arreglo[self.__cantidad] = movilidad
            self.__cantidad += 1
    def cargar(self):
        archivo = open("movilidades.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            patente = fila[0]
            tipo = fila[1]
            capacidad = fila[2]
            importe = fila[3]
            marca = fila[4]
            modelo = fila[5]
            self.agregar(Movilidad(patente, tipo, capacidad, importe, marca, modelo))
        archivo.close()

    def listarPatente(self, patente, gg):
        i = 0
        acum = 0
        long = len(self.__arreglo)
        while i < long:
            if self.__arreglo[i].getPatente() == patente:
                acum += float(self.__arreglo[i].getImportePatente())
                self.__arreglo[i].mostrar()
                print("Gastos de movilidad")
                print(f"total: {gg.gastos_patente(patente, acum)}")
                return
            i += 1
    def buscar_por_patente(self, patente):
        i = 0
        long = len(self.__arreglo)  
        while i < long:
            if self.__arreglo[i].getPatente() == patente:
                return self.__arreglo[i]
            i += 1
        
