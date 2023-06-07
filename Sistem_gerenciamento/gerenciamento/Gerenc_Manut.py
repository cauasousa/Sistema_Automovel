from classes.Manutencao import Manutencao
from classes.P_Veiculo import Veiculo
from Sistem_gerenciamento.interface.Interface import Abst_Nivel_l_sist
from random import randint

class Gerenc_Manutencao(Abst_Nivel_l_sist):
    
    def __init__(self) -> None:
        self.__data_base = dict()
        self.__gerador_cod = list()

    def __validar_cod(self, lista, num):
        if not lista: return False
        if(lista[0] == num) : return True
        return self.__validar_cod(lista[1:], num)

    def add(self, custo : float, tipo : str, data : str, veiculo : Veiculo):
        cadast_new = Manutencao(custo, tipo, data, veiculo)
        cod_aleatorio = 0

        while True:
            cod_aleatorio = randint(101, 200)
            if self.__validar_cod(self.__gerador_cod, cod_aleatorio) == False: 
                self.__gerador_cod.append(cod_aleatorio)
                break
        
        self.__data_base[cod_aleatorio] = cadast_new
        print('Seu Código é ', cod_aleatorio)

    def total_manut(self):
        total = 0.0
        
        for i in self.__data_base.values():
            total += float(i.custo)
        
        print("Total gasto com manutenção ", total)
    
    def quant_min(self):
        if(len(self.__gerador_cod) > 0):
            return True
        return False