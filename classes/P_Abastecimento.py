from classes.P_Veiculo import Veiculo

class Abastecimento:
    def __init__(self, veiculo:Veiculo, valor:float, data:str):
        self.__valor = valor
        self.__data = data
        self.__veiculo = veiculo

    @property
    def valor(self):
        return self.__valor
    
    @property
    def data(self):
        return self.__data

    @property
    def veiculo(self):
        return self.__veiculo