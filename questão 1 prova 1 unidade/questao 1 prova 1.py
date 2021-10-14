from funcoes import *
try:
    f = open('dados_pessoas.txt')
    f.close()
except:
    f = open('dados_pessoas.txt','a')
    f.close()
try:
    f = open('dados_maquinas.txt.txt')
    f.close()
except:
    f = open('dados_maquinas.txt','a')
    f.close()






escolha = 1
while escolha != 0:
    print('Escolha uma opção do menu:')
    print()
    print('1 - Cadastrar cliente')
    print('2 - Cadastrar maquina')
    print('3 - Registro de aluguel')
    print('4 - Relatorio de clientes')
    print('5 - Relatorio de maquinas')
    print('6 - Relatório de Reservas')
    print('0 - Sair')
    print()
    escolha = int(input('escolha sua opção: '))

    if escolha == 1:
        try:
            cpf = str(input('Digite o cpf do cliente: '))
            assert len(cpf) == 11
            assert cpf.isnumeric() == True
            nome = str(input('Digite o nome do cliente: ')).capitalize()
            cadastrar_clientes(nome,cpf)
        except AssertionError:
            print('cpf invalido')

    if escolha == 2:
        try:
            codigo = int(input('Digite o codigo da maquina: '))
            tipo = int(input('''
            1 - Perfurador
            2 - Demolidor
            3 - Compactador
            insira a opção desejada: '''))
            marca = str(input('Digite a marca da maquina: '))
            modelo = str(input('Digite o modelo da maquina: '))
            ano = int(input('Digite o ano da maquina: '))
            valor = float(input('Digite o valor do aluguel da maquina: '))
            status = int(input('''
                1 - disponivel
                2 - indisponivel
                Digite a opção desejada: 
            '''))
            cadastrar_maquina(codigo,tipo,marca,modelo,ano,valor,status)
            
        except:
            print('informação invalida')
    
    if escolha == 3:
        
        cpf = str(input('Digite o cpf do cliente: '))
        codigo = str(input('Digite o codigo da maquina: '))
        reservar_maquina(cpf,codigo)

    if escolha == 4:
        relatorio_clientes()
    if escolha == 5:
        relatorio_maquinas()
    if escolha == 6:
        relatorios_reservas()

