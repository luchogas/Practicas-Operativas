class Tramo:
    __origen:str
    __destino:str
    __distancia:int
    __patente:str
    def __init__(self, origen, destino, distancia, patente):
        self.__origen = origen
        self.__destino = destino
        self.__distancia = distancia
        self.__patente = patente
    def getorigen(self):
        return self.__origen
    def getdestino(self):
        return self.__destino
    def getdistancia(self):
        return self.__distancia
    def getpatente(self):
        return self.__patente
    def mostrar(self):
        print(f"origen: {self.__origen}, destino: {self.__destino}, distancia: {self.__distancia}, patente: {self.__patente}")
    def __gt__(self, otro):
        return self.__distancia < otro.getdistancia()