class Colectivo:
    __patenteC:str
    __marca:str
    __modelo:int
    __capacidad:int
    __dni:int
    __consumo = 35
    
    def __init__(self, patenteC, marca, modelo, capacidad, dni):
        self.__patenteC = patenteC
        self.__marca = marca
        self.__modelo = modelo
        self.__capacidad = capacidad
        self.__dni = dni
        
        
    def getpatentec(self):
        return self.__patenteC
    def getmarca(self):
        return self.__marca
    def getmodelo(self):
        return self.__modelo
    def getcapacidad(self):
        return self.__capacidad
    def getdni(self):
        return self.__dni
    @classmethod
    def getconsumo(cls):
        return cls.__consumo
    def mostrar(self):
        print(f"patente: {self.__patenteC}, marca:{self.__marca}, modelo:{self.__modelo}, capacidad:{self.__capacidad}, dni:{self.__dni}, consumo cada 100km:{self.__consumo}")
        