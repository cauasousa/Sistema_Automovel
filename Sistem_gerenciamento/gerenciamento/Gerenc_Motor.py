from classes.P_Motorista import Motorista
from Sistem_gerenciamento.interface.Interface import Abst_Nivel_3_sist

class Gerenciamento_Motorista(Abst_Nivel_3_sist):
    
    def __init__(self) -> None:
        self.__database = dict()
        self.__quant_motorista = 0

    def add(self, nome:str, cpf, rg, cnh):  
        motorista_new = Motorista(nome, cpf, rg, cnh)
        self.__database[cpf] = motorista_new
        self.__quant_motorista +=1

    def find(self, cpf):
        if self.__quant_motorista > 0:
            find_motot = self.__database.get(cpf)

            if(find_motot == None):
                print("\033[4;31mMotorista Não Encontrado!\033[m")
                return None
            
            return find_motot
        else:
            print("\033[4;31mAdicione Motorista!\033[m")
    
    def editar(self, opc:int, motorista:Motorista, novo):
        """
        OPC:\n
            1 - nome\n
            2 - RG\n
            3 - CNH
        """
        if self.__quant_motorista > 0:

            if(motorista == None):
                print("USUA NOT FIND")
                return 
            if(opc == 1):
                motorista.nome = novo
            if(opc == 2):
                motorista.rg = novo
            if(opc == 3):
                motorista.cnh = novo
        else:
            print("\033[4;31mAdicione Motorista!\033[m")
          
    def deletar(self, motorista:Motorista):

        if(self.__quant_motorista > 0):
            
            if(motorista != None):
                del self.__database[motorista.cpf]
                self.__quant_motorista -= 1
                print("\033[4;31mDeletado!\033[m")
        else:
            print("\033[4;31mAdicione Motorista!\033[m")
    
    def quant_min(self):
        if self.__quant_motorista > 0:
            return True
        return False
    
    @property
    def quant_motorista(self):
        return self.__quant_motorista