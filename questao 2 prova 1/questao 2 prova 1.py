from funcoes import *
import mysql.connector
banco = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='aps 1'
)
cursor = banco.cursor()


try:
    f = open('dados_veterinarios.txt')
    f.close()
except:
    f = open('dados_veterinarios.txt','a')
    f.close()
try:
    f = open('dados_animais.txt.txt')
    f.close()
except:
    f = open('dados_animais.txt','a')
    f.close()
try:
    f = open('consultas.txt')
    f.close()
except:
    f = open('consultas.txt','a')
    f.close()




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
        sexo = converter_sexo(sexo)
        status = converter_status(status)
        
        
        
        comando = f"INSERT INTO dados_veterinarios (CFMV,nome,cpf,sexo,situação) VALUES ('{cfmv}','{nome}','{cpf}','{sexo}','{status}')"
        cursor.execute(comando)
        banco.commit()
        
        
        
        
        
    if escolha == 2:
        cfmv = str(input('Digite o CFMV do veterinário: '))
        inativar_veterinario(cfmv)


    if escolha == 3:
        try:
            codigo = str(input('Digite o código de cadastro: '))
            nome = str(input('Digite o nome do animal: '))
            raca = int(input('''1 - Cachorro
2 - Gato
3 - Pássaro
Digite sua opção: '''))
            assert raca in [1,2,3]
            cadastrar_pet(codigo,nome,raca)
        except:
            (print('Informação inválida'))


    if escolha == 4:
        try:
            dia = int(input('Digite o dia da consulta: '))
            assert 0 < dia < 32
            mes = int(input('Digite o mês da consulta: '))
            assert 0 < mes < 13
            cfmv = str(input('Digite o CFMV: '))
            codigo = str(input('Digite o código do pet: '))
            data = f'{dia}/{mes}'
            cadastrar_consulta(data,cfmv,codigo)
        except:
            ('Informação inválida')


    if escolha == 5:
        try:
            dia = int(input('Digite o dia da consulta: '))
            assert 0 < dia < 32
            mes = int(input('Digite o mês da consulta: '))
            assert 0 < mes < 13
            cfmv = str(input('Digite o CFMV: '))
            codigo = str(input('Digite o código do pet: '))
            data = f'{dia}/{mes}'
            inativar_consulta(data,cfmv,codigo)
        except :
            print('informação inválida')


    if escolha == 6:
        relatorio_pets()
    if escolha == 7:
        print('Relatorio de veterinários ativos')
        arquivo = open('dados_veterinarios.txt', 'r')
        for n in arquivo:
            dados = n.split()
            if len(dados) > 0:
                if int(dados[4]) == 1:
                    sexo = converter_sexo(int(dados[3]))
                    print(f'CFMV:{dados[0]}---Nome:{dados[1]}----CPF:{dados[2]}-----Sexo:{sexo}')
    if escolha == 8:
        dia = int(input('Digite o dia da consulta: '))
        assert 0 < dia < 32
        mes = int(input('Digite o mês da consulta: '))
        assert 0 < mes < 13
        data = f'{dia}/{mes}'
        relatorios_consultas(data)