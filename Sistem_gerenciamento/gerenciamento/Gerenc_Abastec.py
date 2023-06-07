from classes.P_Veiculo import Veiculo
from classes.P_Abastecimento import Abastecimento
from Sistem_gerenciamento.interface.Interface import Abst_Nivel_l_sist
from random import randint

class Gerenciamento_Abastecimento(Abst_Nivel_l_sist):
    
    def __init__(self) -> None:
        self.__data_base = dict()
        self.__gerador_cod = list()

    def __validar_cod(self, lista, num):
        if not lista: return False
        if(self.__gerador_cod[0] == num) : return True
        return self.__validar_cod(lista[1:], num)

    def add(self, valor : float, data : str, veiculo : Veiculo):
        abast_new = Abastecimento(veiculo, valor, data)
        cod_aleatorio = 0

        while True:
            cod_aleatorio = randint(201, 300)
            if self.__validar_cod(self.__gerador_cod, cod_aleatorio) == False: 
                self.__gerador_cod.append(cod_aleatorio)
                break

        self.__data_base[cod_aleatorio] = abast_new
        print('Seu Código é ', cod_aleatorio)
        
    def total_abast(self):
        total = 0.0
        for i in self.__data_base.values():
            total += float(i.valor)
        print("Total gasto com abastecimento ", total)
    
    def quant_min(self):
        if(len(self.__gerador_cod) > 0):
            return True
        return False