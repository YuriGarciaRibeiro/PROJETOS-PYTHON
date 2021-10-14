from tabulate import tabulate

def converter_sexo(sexo):#converte o numero no arquivo txt ao sexo equivalente
    if sexo == 1:
        return 'Masculino'
    elif sexo == 2:
        return 'Feminino'


def converter_raca(raca):#converte o numero no arquivo txt a raça equivalente
    if raca == 1:
        return 'Cachorro'
    elif raca == 2:
        return 'Gato'
    elif raca == 3:
        return 'Pássaro'


def validar_cpf():#valida o cpf de acordo com o o padrao brasileiro
    cpf = 'a'
    while cpf.isnumeric() == False or len(cpf) != 11:
        cpf = input("Digte o CPF do veterinário: ")
        if cpf.isnumeric() == False or len(cpf) != 11:
            print('Informação inválida')
    return cpf


def converter_status(status):#converte o numero no arquivo txt ao status equivalente
    if status == 1:
        return 'Disponivel'
    elif status == 2:
        return 'Indisponivel'


def cadastrar_consulta(data,cfmv,codigo,cursor,banco):
    comando = f'SELECT * FROM dados_veterinarios where cfmv = {cfmv} '
    cursor.execute(comando)
    dados = cursor.fetchall()
    try:
        if compararString(dados[0][4], 'disponivel') == True:
            lista = [dados[0][0], 0, 0, dados[0][1], 0, data]
            comando = f'SELECT * FROM dados_pets where codigo = {codigo} '
            cursor.execute(comando)
            dados = cursor.fetchall()
            preço = definir_preço(str(dados[0][2]).lower())

            lista[1] = codigo
            lista[2] = preço
            lista[4] = dados[0][1]

            comando = 'INSERT INTO dados_consultas (cfmv,codigo_pet,valor,nome_vet,nome_pet,data,situação) VALUES (%s,%s,%s,%s,%s,%s,DEFAULT)'
            dados = (lista[0], lista[1], lista[2], lista[3], lista[4], lista[5])
            cursor.execute(comando, dados)
            banco.commit()
            print('='*25)
            print('CADASTRO DE CONSULTA REALIZADO COM SUCESSO')
            print('=' * 25)
    except IndexError:
        print('=' * 25)
        print('VETERINARIO NÃO CADASTRADO')
        print('=' * 25)


def compararString(a, b):
    i = 0
    while i < len(a):
        if a[i] != b[i]:
            return False
            break
        i += 1
    return True

def definir_preço(raca):
    if compararString(raca,'cachorro') == True:
        return 100
    elif compararString(raca,'gato') == True:
        return  120
    elif compararString(raca,'passaro') == True or compararString(raca,'pássaro') == True:
        return  150


def tabela_consultas(cursor):
    comando = f'SELECT * FROM dados_consultas'
    cursor.execute(comando)
    dados = cursor.fetchall()
    print(tabulate(dados, headers=["ID", "CFMV", "CODIGO DO PET","VALOR","NOME DO VETERINARIO","NOME DO PET","DATA","STATUS"], tablefmt='fancy_grid'))


def tabela_pets(cursor):
    comando = f'SELECT * FROM dados_pets'
    cursor.execute(comando)
    dados = cursor.fetchall()
    print(tabulate(dados, headers=["CODIGO", "NOME", "RAÇA"], tablefmt='fancy_grid'))


def tabelas_veterinarios_ativos(cursor):
    comando = f'SELECT * FROM dados_veterinarios where situação = "disponivel"'
    cursor.execute(comando)
    dados = cursor.fetchall()
    if len( dados) > 0:
        print(tabulate(dados, headers=["CFMV", "NOME", "CPF","SEXO","SITUAÇÂO"], tablefmt='fancy_grid'))
    else:
        print('=' * 25)
        print('NENHUM VETERINARIO DISPONIVEL')
        print('=' * 25)


def tabelas_veterinarios(cursor):
    comando = f'SELECT * FROM dados_veterinarios'
    cursor.execute(comando)
    dados = cursor.fetchall()
    if len(dados) > 0:
        print(tabulate(dados, headers=["CFMV", "NOME", "CPF", "SEXO", "SITUAÇÂO"], tablefmt='fancy_grid'))
    else:
        print('=' * 25)
        print('NENHUM VETERINARIO CADASTRADO')
        print('=' * 25)

def tabelas_consultas_dia(cursor,data):
    comando = f'SELECT * FROM dados_consultas where data = {data}'
    cursor.execute(comando)
    dados = cursor.fetchall()
    if len(dados) > 0:
        print(tabulate(dados, headers=["CFMV", "NOME", "CPF", "SEXO", "SITUAÇÂO"], tablefmt='fancy_grid'))
    else:
        print('=' * 25)
        print('NENHUMA CONSULTA NESSE DIA')
        print('=' * 25)