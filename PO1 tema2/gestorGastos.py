from claseGastos import Gasto
import csv
class GestorGastos:
    __lista = list
    def __init__(self):
        self.__lista = []

    def mostrar(self):
        for gasto in self.__lista:
            gasto.mostrar()
    def cargar(self):
        archivo = open("gastosAbril2025.csv")
        reader = csv.reader(archivo, delimiter=';')
        next(reader)
        for fila in reader:
            patente = fila[0]
            fecha = fila[1]
            importe = fila[2]
            descripcion = fila[3]
            self.__lista.append(Gasto(patente, fecha, importe, descripcion))
        archivo.close()
    def gastos_patente(self, patente, acum):
        i = 0
        total = 0
        long = len(self.__lista)
        while i < long:
            if self.__lista[i].getPatente() == patente:
                self.__lista[i].mostrar()
                total += float(self.__lista[i].getImporte())
                total += acum
            i += 1
        return total
    def mostrar_por_fecha(self, fecha):
        i = 0
        acum = 0
        long = len(self.__lista)
        while i < long:
            if self.__lista[i].getFecha() == fecha:
                self.__lista[i].mostrar()
                acum += float(self.__lista[i].getImporte())
            i += 1
        print(f"total a pagar en {fecha}: {acum}")
     
            
    def resumen_por_fecha(self, fecha, gm):
        self.__lista.sort()
        i = 0
        long = len(self.__lista)
        while i < long:
            if self.__lista[i].getFecha() == fecha:
                movilidad = gm.buscar_por_patente(self.__lista[i].getPatente())
                movilidad.mostrar()
                total = movilidad.getImportePatente() + self.__lista[i].getImporte()
                print(f"Total a pagar: {total:.2f}")
       
                
            