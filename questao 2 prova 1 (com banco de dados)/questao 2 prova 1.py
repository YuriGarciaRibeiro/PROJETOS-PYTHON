from funcoes import *
import mysql.connector
import datetime

banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='aps 1'
)
cursor = banco.cursor()


escolha = 1
while escolha != 0:
    print('Escolha uma opção do menu:')
    print()
    print('1 - Cadastrar veterinário')
    print('2 - Inativar veterinário')
    print('3 - Cadastrar pet')
    print('4 - Registrar consulta')
    print('5 - Cancelar consulta')
    print('6 - Relatório de pets')
    print('7 - Relatório de veterinários')
    print('8 - Relatório de consultas do dia')
    print('0 - Sair')
    print()
    escolha = int(input('Escolha sua opção: '))


    if escolha == 1:
        cfmv = str(input('Digite o CFMV do veterinário: '))
        nome = str(input('Digite o nome do veterinário: '))
        cpf = validar_cpf()
        sexo = int(input('''1 - Masculino
2 - Feminino
Digite sua opção: '''))
        assert sexo == 1 or sexo == 2
        status = int(input('''1 - Disponivel
2 - Indisponivel
Digite sua opção: '''))
        assert status == 1 or status == 2
        sexo = str(converter_sexo(sexo))
        status = str(converter_status(status))
        cpf = str(cpf)

        dados = (f'{cfmv}',f'{nome}',f'{cpf}',f'{sexo}',f'{status}')
        comando = 'INSERT INTO dados_veterinarios (CFMV,nome,cpf,sexo,situação) VALUES (%s,%s,%s,%s,%s)'
        cursor.execute(comando,dados)
        banco.commit()

    if escolha == 2:
        tabelas_veterinarios(cursor)
        cfmv = str(input('Digite o CFMV do veterinário: '))
        comando = f"UPDATE dados_veterinarios set situação = 'Indisponivel' where CFMV = {cfmv}"
        cursor.execute(comando)
        banco.commit()


    if escolha == 3:
        try:
            nome = str(input('Digite o nome do animal: ')).capitalize()
            raca = int(input('''1 - Cachorro
2 - Gato
3 - Pássaro
Digite sua opção: '''))

            raca = converter_raca(raca)
            dados = (f'{nome}', f'{raca}')
            comando = 'INSERT INTO dados_pets (codigo,nome,raça) VALUES (DEFAULT ,%s,%s)'
            cursor.execute(comando, dados)
            banco.commit()
            tabela_pets(cursor)
        except AssertionError:
            print('=' * 25)
            print('INFORMAÇÃO INVALIDA')
            print('=' * 25)




    if escolha == 4:
        try:
            dia = int(input('Digite o dia da consulta: '))
            assert 0 < dia < 32
            mes = int(input('Digite o mês da consulta: '))
            assert 0 < mes < 13
            cfmv = str(input('Digite o CFMV: '))
            codigo = str(input('Digite o código do pet: '))
            date = datetime.date.today()
            ano = date.strftime("%Y")
            data = f'{ano}-{mes}-{dia}'
            cadastrar_consulta(data,cfmv,codigo,cursor,banco)
            tabela_consultas(cursor)
        except AssertionError:
            print('=' * 25)
            print('INFORMAÇÃO INVALIDA')
            print('=' * 25)




    if escolha == 5:
        tabela_consultas(cursor)
        id = int(input('Digite a identidicação da consulta: '))
        comando = f"UPDATE dados_consultas set situação = 'desativada' where id = {id} "
        cursor.execute(comando)
        banco.commit()
        print('Consulta desativada')


    if escolha == 6:
        tabela_pets(cursor)
    if escolha == 7:
        print('Relatorio de veterinários ativos')
        tabelas_veterinarios_ativos(cursor)
    if escolha == 8:
        tabela_consultas(cursor)