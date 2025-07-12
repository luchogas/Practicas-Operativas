class Gasto:
    __patente: str
    __fecha: str
    __importe: float
    __descripcion: str

    def __init__(self, patente, fecha, importe, descripcion):
        self.__patente = patente
        self.__fecha = fecha
        self.__importe = float(importe)
        self.__descripcion = descripcion

    def getPatente(self): return self.__patente
    def getFecha(self): return self.__fecha
    def getImporte(self): return self.__importe
    def getDescripcion(self): return self.__descripcion

    def mostrar(self):
        print(f"fecha: {self.__fecha}, importe: {self.__importe}, descripcion: {self.__descripcion}")

    def __lt__(self, otro):
        result=None
        if self.__fecha == otro.getFecha():
            result = self.__patente<otro.getPatente()
        else:
            result = self.__fecha<otro.getFecha()
        return result