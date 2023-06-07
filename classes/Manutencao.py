from classes.P_Veiculo import Veiculo

class Manutencao:
    def __init__(self, custo : float, tipo : str, data : str, veiculo : Veiculo):
        self.custo = custo
        self.tipo = tipo
        self.data = data
        self.veiculo = veiculo