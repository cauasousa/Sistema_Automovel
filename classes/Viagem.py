from classes.P_Veiculo import Veiculo
from classes.P_Motorista import Motorista


class Viagem:    
    def __init__(self, origem:str, destino:str,  distancia:float , motorista : Motorista, veiculo : Veiculo):
        self.destino = destino
        self.origem = origem
        self.distancia = distancia
        self.motorista = motorista
        self.veiculo = veiculo