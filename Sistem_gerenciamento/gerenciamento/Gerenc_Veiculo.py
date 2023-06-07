from classes.P_Veiculo import Veiculo
from Sistem_gerenciamento.interface.Interface import Abst_Nivel_3_sist

class GerenciamentoVeiculo(Abst_Nivel_3_sist):

    def __init__(self) -> None:
        self.__database = dict()
        self.__quant_veiculo = 0

    def add(self, marca, modelo, ano, placa, chassi, cor, Km: float):
        new_veicu = Veiculo(marca, modelo, ano, placa, chassi, cor, Km)
        self.__database[placa] = new_veicu
        __quant_veiculo+=1

    def find(self, placa):
        find_veicu = self.__database.get(placa)

        if(find_veicu == None):
            print("Veiculo Não Encontrado!")
        return find_veicu

    def editar(self, opc:int, Objeto_Find : Veiculo, novo):
        """
            EDITAR\n
            1 - Marca     || 4 - Chassi\n
            2 - Modelo    || 5 - Cor\n
            3 - Ano 
        """
        if(Objeto_Find == None):
            print("USUA NOT FIND")
            return 
        if 6 < opc > 0:
            if(opc == 1):
                Objeto_Find.marca = novo
            if(opc == 2):
                Objeto_Find.modelo = novo
            if(opc == 3):
                Objeto_Find.ano = novo
            if(opc == 4):
                Objeto_Find.chassi = novo
            if(opc == 5):
                Objeto_Find.cor = novo

    def deletar(self, Objeto_Find: Veiculo):
    
        if(Objeto_Find == None):
            print("USUA NOT FIND")
            return 
    
        del self.__database[Objeto_Find.placa]
        self.__quant_veiculo-=1

    def see_km_veic(self, placa):
        ref = self.find(placa)
        if None in ref:
            print("\033[4;31mThe Km is ", ref.km,'\033[m')
        else:
            print("\033[4;31mNot Find Veiculo!\033[m")

    def maior_Km_veiculo(self):
        placa = '**'
        Km_maior = 0
        
        for i in self.__database.values():
            if (i.Km >= Km_maior):
                Km_maior = i.Km
                placa = i.placa
        if not placa:
            print('O Veiculo da Placa ', placa, 'Rodou ', Km_maior)
    
    def quant_min(self):
        if self.__quant_veiculo > 0:
            return True
        return False
    
    @property
    def quant_veiculo(self):
        return self.__quant_veiculo