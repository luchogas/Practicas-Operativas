class Movilidad:
    __patente: str
    __tipo: str
    __capacidad: float
    __importe_patente: float
    __marca: str
    __modelo: str

    def __init__(self, patente, tipo, capacidad, importe, marca, modelo):
        self.__patente = patente
        self.__tipo = tipo
        self.__capacidad = float(capacidad)
        self.__importe_patente = float(importe)
        self.__marca = marca
        self.__modelo = modelo

    def getPatente(self): return self.__patente
    def getTipo(self): return self.__tipo
    def getCapacidad(self): return self.__capacidad
    def getImportePatente(self): return self.__importe_patente
    def getMarca(self): return self.__marca
    def getModelo(self): return self.__modelo

    def mostrar(self):
        print(f"Patente: {self.__patente} Tipo: {self.__tipo} Capacidad de Carga: {self.__capacidad}")
        print(f"Importe Mensual de Patente: {self.__importe_patente} Marca: {self.__marca} Modelo: {self.__modelo}")
