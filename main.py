from Sistem_gerenciamento.gerenciamento.Gerenc_Motor import Gerenciamento_Motorista as G_Motorista
from Sistem_gerenciamento.gerenciamento.Gerenc_Manut import Gerenc_Manutencao as G_Manutencao
from Sistem_gerenciamento.gerenciamento.Gerenc_Abastec import Gerenciamento_Abastecimento as G_Abastecimento
from Sistem_gerenciamento.gerenciamento.Gerenc_Veiculo import GerenciamentoVeiculo as G_Veiculo
from Sistem_gerenciamento.gerenciamento.Gerenc_Viagem import Gerenciamento_Viagem as G_Viagem


def relatorio(self_abast : G_Abastecimento, self_manut : G_Manutencao,self_viagem : G_Viagem, self_veiculo : G_Veiculo, self_Motor : G_Motorista):

    # Quantidade de Motorista
    # Quantidade de Veículos
    # Motorista que mais realizou viagens
    # Motorista que mais Km percorreu
    # Veículo com maior Km
    # Total de despesas com abastecimento
    # Total de despesas de Manutenção
    print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    quant_moto = self_Motor.quant_motorista
    quant_veic = self_veiculo.quant_veiculo
    print('Quantidade de Motorista: ', quant_moto)
    print('Quantidade de Veiculo: ', quant_veic)

    self_viagem.Motorista_realizou_vigens()
    self_viagem.motorista_maior_Km()
    self_veiculo.maior_Km_veiculo()
    self_abast.total_abast()
    self_manut.total_manut()
    print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

def menu_gerenciamento_motorista(self : G_Motorista):

    print(''' 
    \033[1;30;46ma. Cadastrar Novo Motorista\033[m
    \033[1;30;46mb. Pesquisar Motorista\033[m
    \033[1;30;46mc. Editar Motorista\033[m
    \033[1;30;46md. Deletar Motorista\033[m
    ''')

    opc = input("\t\033[1;35m>>>>>>\033[m")
    if('a' in opc):
        name = input("Nome: ")
        cpf = input("CPF: ")
        rg = input("RG: ")
        cnh = input("CNH: ")
        self.add(name, cpf, rg, cnh)

    elif('b' in opc and self.quant_min()):
        cpf = input("CPF do motorista: ")
        ref = self.find(cpf)
        if None != ref:
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            print("Nome: ", ref.nome)
            print("CPF: ", ref.cpf)
            print("RG: ", ref.rg)
            print("CNH: ", ref.cnh)
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

    elif('c' in opc and self.quant_min()):
        cpf = input("CPF do motorista: ")
        ref = self.find(cpf)
        if None != ref:
            print("Write for Edit:\n\t 1 - Name\n\t 2 - RG\n\t 3 - CNH")
            opc = int(input('>>>>> '))

            if(4 < opc > 0):
                alteracao = input("Write new change: ")
                self.editar(opc, ref, alteracao)
              
    elif('d' in opc and self.quant_min()):
        cpf = input("CPF do motorista: ")
        ref = self.find(cpf)
        if None not in ref:
            self.deletar(ref)

def menu_gerenciamento_veiculos(self : G_Veiculo):
    
    print(''' 
    \033[1;30;46ma. Cadastrar Veículo\033[m
    \033[1;30;46mb. Pesquisar Veículo\033[m
    \033[1;30;46mc. Editar Veículo\033[m
    \033[1;30;46md. Deletar Veículo\033[m
    \033[1;30;46me. Ver quilometragem de Veículo\033[m
    m
    ''')
    
    opc = input("\t>>>>>> ")
    if('a' in opc):
        marca = input("Marca: ")
        modelo = input("Modelo: ")
        ano = input("Ano: ")
        placa = input("Placa: ")
        chassi = input("chassis: ")
        cor = input("COR: ")
        km = input("KM: ")
        self.add(marca, modelo, ano, placa, chassi, cor, km)

    elif('b' in opc and self.quant_min()):
        placa = input("Placa do veiculo: ")
        ref = self.find(placa)

        if None != ref:
            print('\n=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
            print("Marca: ", ref.marca)
            print("Modelo: ", ref.modelo)
            print("Ano: ", ref.ano)
            print("Placa: ", ref.placa)
            print("Chassi: ", ref.chassi)
            print("Cor: ", ref.cor)
            print("Km: ", ref.km)
            print('=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n')

    elif('c' in opc and self.quant_min()):
        placa = input("Placa do veiculo: ")
        ref = self.find(placa)
        if None != ref:
            print("Write for Edit:\n\t 1 - Marca\n\t 2 - Modelo\n\t 3 - Ano\n\t 4 - Chassi\n\t 5 - Cor")
            opc = int(input('>>>>> '))

            if(6 < opc > 0):
                alteracao = input("Write new change: ")
                self.editar(opc, ref, alteracao)

    elif('d' in opc and self.quant_min()):
        placa = input("Placa do veiculo: ")
        ref = self.find(placa)
        if None != ref:
            self.deletar(ref)

    elif('e' in opc and self.quant_min()):
        placa = input("Placa do veiculo: ")
        self.see_km_veic(placa)
        
def gerenciamento_viagem(self : G_Viagem, self_1 : G_Veiculo, self_2 : G_Motorista):
    #destino, origem, distância, motorista e veículo
    print(''' 
    \033[1;30;46ma. Cadastrar Viagem\033[m
    \033[1;30;46mb. Editar Viagem\033[m
    ''')

    opc = input("\t>>>>>> ")
    if('a' in opc and self_1.quant_min() and self_2.quant_min()):
        destino = input("Nome: ")
        origem = input("CPF: ")
        distancia = float(input("RG: "))

        motorista = None
        while True:
            cpf = input("\n\t0 - CLOSE\n\tCPF: ")
            if '0' == cpf:
                return
            
            motorista = self_2.find(cpf)

            if None != motorista :
                break

        veiculo = None
        while True:
            placa = input("\n\t0 - CLOSE\n\tCPF: ")
            if '0' == placa:
                return
            
            veiculo = self_1.find(placa)

            if None != veiculo :
                break
            
        self.add(destino, origem, distancia, motorista, veiculo)
    
    elif('b' in opc and self.quant_min()):
        cod = input("Código Viagem: ")
        print("Write for Edit:\n\t 1 - Origem\n\t 2 - Destino\n\t 3 - Distancia")
        opc = int(input('>>>>> '))

        if(4 < opc > 0):
            alteracao = input("Write new change: ")
            if opc == 3:
                alteracao = float(alteracao)

            self.editar(opc, cod, alteracao)

def menu_principal(self_abast : G_Abastecimento, self_manut : G_Manutencao,self_viagem : G_Viagem, self_veiculo : G_Veiculo, self_Motor : G_Motorista):
    # 4 -> data, quantidade de combustível, valor, entre outros.
    
    print('''
    \033[1;30;46m1. Gerenciamento de Motoristas\033[m
    \033[1;30;46m2. Gerenciamento de Veículos\033[m
    \033[1;30;46m3. Gerenciamento de  Viagem\033[m
    \033[1;30;46m4. Registrar Abastecimento\033[m
    \033[1;30;46m5. Registrar Manutenção\033[m
    \033[1;30;46m6. Relatório\033[m
    ''')
    

    opc = int(input(">>>>>> "))
    if(opc == 1):
        menu_gerenciamento_motorista(self_Motor)

    elif(opc == 2):
        menu_gerenciamento_veiculos(self_veiculo)

    elif(opc == 3 and self_Motor.quant_min() and self_veiculo.quant_min()):
        gerenciamento_viagem(self_viagem, self_veiculo, self_Motor)

    elif(opc == 4 and self_veiculo.quant_min()):

        veiculo = None
        while True:
            placa = input("\n\t0 - CLOSE\n\tCPF: ")
            if '0' == placa:
                return True
            
            veiculo = self_veiculo.find(placa)

            if None != veiculo :
                break
        
        valor = float(input('Valor: '))
        data = input('Data: ')
        self_abast.add(valor, data, veiculo)

    elif(opc == 5 and self_veiculo.quant_min()):
        veiculo = None
        while True:
            placa = input("\n\t0 - CLOSE\n\tCPF of Veiculo : ")
            if '0' == placa:
                return True
            
            veiculo = self_veiculo.find(placa)

            if None != veiculo :
                break
        
        custo = float(input('Custo: '))
        tipo = input('Type: ')
        date = input('Date: ')
        self_manut.add(custo, tipo, date, veiculo)

    elif(opc == 6):
        relatorio(self_abast, self_manut, self_viagem, self_veiculo, self_Motor)
        pass
    elif opc == 0:
        return False
    return True

############# MAIN ###############
cond = True
R_abast = G_Abastecimento()
R_manut = G_Manutencao()
R_motori = G_Motorista()
R_veicul = G_Veiculo()
R_viagem = G_Viagem()

while cond != False:  
    cond = menu_principal(R_abast, R_manut, R_viagem, R_veicul, R_motori)
