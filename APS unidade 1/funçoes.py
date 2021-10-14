from time import sleep
from os import system

def linha(x):
    print('='*x)
def criar_vagas(filas, coluna):#cria uma matriz que é equivalente as vagas
    matriz = []
    for n in range(filas):
        linha = []
        for n in range(coluna):
            linha.append(0)
        matriz.append(linha)
    return matriz


def vagas_disponiveis(matriz):#cria uma lista com as vagas disponiveis 
    disponiveis = []
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == False:
                disponiveis.append(j + 1)
        print(f'Fila {i + 1}: {disponiveis}')
        disponiveis = []


def cadastrar_cliente(nome,cpf):#adciona o nome e cpf do cliente no arquivo txt sem a vaga
    sleep(1)
    linha(30)
    arquivo_dados = open('dados.txt', 'a')
    arquivo_dados.write(f'{nome} {cpf} a b\n')
    arquivo_dados.close()
    print('Cliente cadastrado')

def consultar_clientes(cpf):#consulta o nome do cliente baseado no cpf no arquivo txt
    sleep(1)
    linha(30)
    arquivo_dados = open('dados.txt', 'r')
    for dados_clientes in arquivo_dados:
        dados = dados_clientes.split()
        if cpf == dados[1]:
            print(f'nome:{dados[0]}---CPF:{dados[1]}')
    arquivo_dados.close()

def reservar_vaga(matriz,cpf,fileira,coluna):#adciona o a fileira e a coluna da cadeira desejada no arquivo txt
    sleep(1)
    linha(30)
    dados_temporarios = list()

    if matriz[fileira - 1][coluna - 1] == 1:
        print('Essa vaga ja esta ocupada, tente novamente')
    else:
        contador = -1
        arquivo_dados = open('dados.txt', 'r')
        for n in arquivo_dados:
            dados_temporarios.append(n)
            contador += 1
            dados = n.split()
            if int(dados[1]) == int(cpf):
                if dados[2].isnumeric() == True:
                    print('Essa pessoas ja tem uma vaga reservada')
                elif dados[2].isnumeric() == False:
                    dados_temporarios[contador] = f'{dados[0]} {dados[1]} {fileira} {coluna}\n'
                    matriz[fileira-1][coluna-1] = 1
        arquivo_dados.close()
        arquivo_dados = open('dados.txt', 'w')
        for n in dados_temporarios:
            arquivo_dados.write(n)
        arquivo_dados.close()
        print('Vaga reservada')

def excluir_reserva(cpf,matriz):#troca a cadeira e a fileira no arquivo txt e salva essa fileira e cadeira na lista de cadeira canceladas
    sleep(1)
    linha(30)
    dados_temporarios = list()
    arquivo_dados = open('dados.txt', 'r')
    for n in arquivo_dados:
        dados = n.split()
        if int(dados[1]) == int(cpf):
            matriz.append(f'fileira {dados[2]} coluna {dados[3]}')
            dados_temporarios.append(f'{dados[0]} {dados[1]} a b\n')
        elif int(dados[1]) != int(cpf):
            dados_temporarios.append(n)
    arquivo_dados.close()
    arquivo_dados = open('dados.txt', 'w')
    for n in dados_temporarios:
        arquivo_dados.write(n)
    arquivo_dados.close()
    print('Reserva Excluida')

def relatorio_reservas():#mostra todas as vagas que estao ocupadas com seus respectivos donos
    sleep(1)
    linha(30)
    print('Relatorio de reservas')
    arquivo_dados = open('dados.txt', 'r')
    for n in arquivo_dados:
        dados = n.split()
        if dados[2].isnumeric() == True:
            print(f'Nome:{dados[0]} CPF:{dados[1]} fileira {dados[2]} cadeira {dados[3]}')

def relatorio_canelados(matriz):#mostra todas as cadeiras canceladas a partir do inicio do programa
    print('Relatorio de cancelamento')
    for n in matriz:
        print(f'o lugar {n} foi cancelado')

def salvar_reservas_arquivo_dados(matriz):#transfere as vagas reservadas para a lista dentro do programa
    arquivo_dados = open('dados.txt', 'r')
    for dados_clientes in arquivo_dados:
        dados = dados_clientes.split()
        if dados[2].isnumeric() == True:
            fileira = int(dados[2])
            if dados[3].isnumeric() == True:
                coluna = int(dados[3])
                matriz[fileira - 1][coluna - 1] = 1
    arquivo_dados.close()