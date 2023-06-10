import Sistem_gerenciamento.gerenciamento.Classe_Ger as GR
from classes.Viagem import Viagem


class Gerenciamento_Viagem(GR.Gerenciamento_N2):
    def __init__(self):
        super().__init__()

    def editar(self, viagem, alteracao, opc:int):
        """opc:
            1 - Origem\n 
            2 - Destino\n
            3 - Distancia\n
        """
        
        if None != viagem:
            if(opc == 1):
                viagem.origem = alteracao
            if(opc == 2):
                viagem.destino = alteracao
            if(opc == 3):
                alteracao = float(alteracao)
                if(alteracao >= 0.0):
                    aux = alteracao - viagem.distancia
                    viagem.distancia = alteracao
                    viagem.veiculo.km += aux
                else:
                    print('\t\t\033[1;31mImpossível Ter Distancia Negativa. Informe Um Valor Maior que Igual ou Maior que Zero, Por favor!\033[m')
            print("\t\t\033[1;31mATUALIZADO !!\033[m")
        else:
            print("\t\t\033[1;31mNot Find\033[m")

    def motorista_maior_Km(self):
        name = {}        

        for i in self._data_base.values():
            con = 0
            if i.motorista.cpf not in name:
                name.update({i.motorista.cpf: [i.motorista.nome, i.distancia]})
            else: 
                con = name[i.motorista.cpf][1] + i.distancia
                name.update({i.motorista.cpf:[i.motorista.nome, con]})

        aux = 0
        moto = list()
        for i in name.values():
            if(aux == i[1]):
                moto.append(i[0])
            elif aux < i[1]:
                aux = i[1]
                moto.clear()
                moto.append(i[0])

        if(len(moto) == 0):
            print('\t\t\033[1;31mNão tem Motorista com maior KM\033[m')
        else:
            print('\t\t\033[1;34mMotorista(s) com maior(es) Km: ', end='')
            design = 0
            for i in moto:
                print(i, end=' ')
                design+=1
                if(len(moto) > design and len(moto) > 0):
                    print(',', end=' ')
            print('com', aux, 'KM', '\033[m')
    
    def Motorista_realizou_vigens(self):
        name = {}
        
        for i in self._data_base.values():
            con = 0
            if i.motorista.cpf not in name:
                name.update({i.motorista.cpf: [i.motorista.nome, 1]})
            else: 
                con = name[i.motorista.cpf][1] + 1
                name.update({i.motorista.cpf:[i.motorista.nome, con]})

        aux = 0
        moto = list()
        for i in name.values():
            if(aux == i[1]):
                moto.append(i[0])
            elif aux < i[1]:
                aux = i[1]
                moto.clear()
                moto.append(i[0])

        if(len(moto) == 0):
            print('\t\t\033[1;31mNão Houve Cadastro de Viagem\033[m')
        else:
            print('\t\t\033[1;34mMotorista(s) que mais realiza(ram) viagens: ', end='')
            design = 0
            for i in moto:
                print(i, end=' ')
                design+=1
                if(len(moto) > design and len(moto) > 0):
                    print(',', end=' ')
            print('com', aux, 'viagens', '\033[m')
