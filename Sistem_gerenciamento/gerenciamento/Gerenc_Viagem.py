from classes.Viagem import Viagem
from classes.P_Veiculo import Veiculo
from classes.P_Motorista import Motorista
from Sistem_gerenciamento.interface.Interface import Abst_Nivel_2_sist
from random import randint


class Gerenciamento_Viagem(Abst_Nivel_2_sist):
    
    def __init__(self) -> None:
        self.__data_base = dict()
        self.__gerador_cod = list()

    def __validar_cod(self, lista, num):
        if not lista: return False
        if(self.__gerador_cod[0] == num) : return True
        return self.__validar_cod(lista[1:], num)

    def add(self, destino:str, origem:str, distancia:float, motorista : Motorista, veiculo : Veiculo):
        viagem = Viagem(origem, destino, distancia, motorista, veiculo)
        veiculo.Km+=distancia        
        cod_aleatorio = 0
        
        while True:
            cod_aleatorio = randint(1, 100)
            if(self.__validar_cod(self.__gerador_cod, cod_aleatorio) == False): 
                self.__gerador_cod.append(cod_aleatorio)
                break

        self.__data_base[cod_aleatorio] = viagem
        print("O código da Viagem é ", cod_aleatorio)
    
    def __find_viagem(self, cod):
        find_viagem = self.__data_base.get(cod)

        if(find_viagem == None):
            print("Viagem Não Cadastrada!")
        else:
            return find_viagem
        
        return None

    def editar(self, cod:int, alteracao, opc:int):
        """opc:
            1 - Origem\n 
            2 - Destino\n
            3 - Distancia\n
        """
        viagem = self.__find_viagem(cod)
        if None not in viagem:
            if(opc == 1):
                viagem.origem = alteracao
            if(opc == 2):
                viagem.destino = alteracao
            if(opc == 3): 
                aux = alteracao - viagem.distancia
                viagem.distancia = alteracao
                viagem.veiculo.Km += aux

            print("ATUALIZADO !!")
        else:
            print("Not Find")

    def motorista_maior_Km(self):
        name = {}
        value = 0
        

        for i in self.__data_base:
            con = 0
            if i.motorista.cpf not in name:
                name.update({i.motorista.cpf: [i.motorista.nome, i.distancia]})
            else: 
                con = name[i.motorista.cpf][1] + i.distancia
                name.update({i.motorista.cpf:[i.motorista.nome, con]})

        aux = 0
        moto = '**'
        for i in name.values():
            if aux < i[1]:
                aux = i[1]
                moto = i[0]

        print('Motorista com maior Km: ', moto, 'com', aux, 'KM')
    
    def Motorista_realizou_vigens(self):
        name = {}

        for i in self.__data_base:
            con = 0
            if i.motorista.cpf not in name:
                name.update({i.motorista.cpf: [i.motorista.nome, 1]})
            else: 
                con = name[i.motorista.cpf][1] + 1
                name.update({i.motorista.cpf:[i.motorista.nome, con]})

        aux = 0
        moto = '**'
        for i in name.values():
            if aux < i[1]:
                aux = i[1]
                moto = i[0]

        print('Motorista que mais realizou viagem: ', moto, 'com', aux, 'viagens')
    
    def quant_min(self):
        if(len(self.__gerador_cod) > 0):
            return True
        return False