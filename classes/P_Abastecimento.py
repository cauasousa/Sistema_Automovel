from classes.P_Veiculo import Veiculo

class Abastecimento:
    def __init__(self, veiculo:Veiculo, valor:float, data:str):
        self.valor = valor
        self.data = data
        self.veiculo = veiculo