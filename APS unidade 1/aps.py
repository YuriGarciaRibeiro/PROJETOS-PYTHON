from funçoes import *


#criando as listas
vagas = criar_vagas(6,10)
cancelados = []

#abrindo arquivo e analisando dados 
salvar_reservas_arquivo_dados(vagas)


escolha = 1
while escolha != 0:
    print('Escolha uma opção do menu:')
    print()
    print('1 - Cadastrar cliente')
    print('2 - Consultar cliente')
    print('3 - Reservar vaga')
    print('4 - Excluir reserva')
    print('5 - Relatório de Reservas')
    print('6 - Relatório de Vagas Livres')
    print('7 - Relatório de Cancelamento de Reservas de Vagas')
    print('0 - Sair')
    print()
    escolha = int(input('escolha sua opção: '))

    if escolha == 1:
        try:
            nome = str(input('Digite o nome do cliente: ')).capitalize()
            cpf = str(input('digite o CPF do cliente: '))
            assert len(cpf) == 11
            cadastrar_cliente(nome, cpf)
        except AssertionError:
            linha(12)
            print('CPF invalido')
            linha(12)



    if escolha == 2:
        try:
            cpf = str(input('digite o CPF do cliente: '))
            assert len(cpf) == 11
            consultar_clientes(cpf)
        except AssertionError:
            linha(12)
            print('CPF invalido')
            linha(12)


    if escolha == 3:
        try:
            cpf = str(input('digite o CPF do cliente: '))
            assert len(cpf) == 11
            fileira = int(input('digite a fileira da vaga: '))
            assert 1 <= fileira <= len(vagas) + 1
            coluna = int(input('digite a coluna da vaga:  '))
            assert  1 <= coluna <= len(vagas[0])
            reservar_vaga(vagas, cpf, fileira, coluna)
        except AssertionError:
            linha(19)
            print('Informação invalida')
            linha(19)

    if escolha == 4:

        try:
            cpf = str(input('digite o CPF do cliente: '))
            assert len(cpf) == 11
            excluir_reserva(cpf,cancelados)
        except AssertionError:
            linha(12)
            print('CPF invalido')
            linha(12)



    if escolha == 5:
        relatorio_reservas()

    if escolha == 6:
        vagas_disponiveis(vagas)

    if escolha == 7:
        relatorio_canelados(cancelados)