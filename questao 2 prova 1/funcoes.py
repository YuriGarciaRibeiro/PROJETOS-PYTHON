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


def alterar_linha(path,codigo,nova_linha):#altera uma linha no arquivo txt fornecendo uma string que vai estar dentro da linha
    with open(path,'r') as f:
        texto=f.readlines()
    with open(path,'w') as f:
        for i in texto:
            if codigo in i:
                f.write(nova_linha+'\n')
            else:
                f.write(i)


def cadastro_veterinario(cfmv,nome,cpf,sexo,status):#cadastra o veterinario com suas informaçoes no arquivo txt
    arquivo_dados = open('dados_veterinarios.txt', 'r')
    cont = 0
    for linha in arquivo_dados:
        dados = linha.split()
        if len(dados) > 0:
            if int(dados[0]) ==  int(cfmv):
                cont += 1
    arquivo_dados.close()
    if cont == 1:
        print('CFMV já cadastrado')
    else:
        arquivo_dados = open('dados_veterinarios.txt', 'a')
        arquivo_dados.write(f'{cfmv} {nome} {cpf} {sexo} {status}\n')
        arquivo_dados.close()
        print('=' * 25)
        print('Veterinário cadastrado')
        print('=' * 25)


def inativar_veterinario(cfmv):#inativa
    arquivo = open('dados_veterinarios.txt','r')
    for n in arquivo:
        dados = n.split()
        if len(dados) > 0:
            if int(dados[0]) == int(cfmv):
                vet = f'{dados[0]} {dados[1]} {dados[2]} {dados[3]} 2'
    try:
        alterar_linha('dados_veterinarios.txt',cfmv,vet)
        print('=' * 25)
        print('Veterinário suspenso')
        print('=' * 25)
    except:
        print('=' * 25)
        print('Veterinário não cadastrado')
        print('=' * 25)


def cadastrar_pet(codigo,nome,especie):
    arquivo_dados = open('dados_animais.txt', 'r')
    cont = 0
    for linha in arquivo_dados:
        dados = linha.split()
        if len(dados) > 0:
            if int(dados[0]) == int(codigo):
                cont += 1
    arquivo_dados.close()
    if cont == 1:
        print('Código ja cadastado')
    else:
        arquivo_dados = open('dados_animais.txt', 'a')
        arquivo_dados.write(f'{codigo} {nome} {especie}\n')
        arquivo_dados.close()
        print('=' * 25)
        print('Animal cadastrado')
        print('=' * 25)


def cadastrar_consulta(data,cfmv,codigo):
    arquivo_dados = open('dados_veterinarios.txt', 'r')
    cont = 0
    for linha in arquivo_dados:
        dados = linha.split()
        if len(dados) > 0:
            if int(dados[0]) == int(cfmv):
                nome_vet = dados[1]
            if int(dados[4]) == 2:
                cont = 1
    arquivo_dados.close()
    arquivo_dados = open('dados_animais.txt', 'r')
    raca = 0
    for linha in arquivo_dados:
        dados = linha.split()
        if len(dados) > 0:
            if dados[0] == codigo:
                raca = int(dados[2])
                nome = dados[1]

    arquivo_dados.close()
    if raca == 1:
        valor = 100
    elif raca == 2:
        valor = 120
    elif raca == 3:
        valor = 150

    if cont == 1:
        print('Veterinário indisponivel')
    else:
        arquivo_dados = open('consultas.txt', 'a')
        arquivo_dados.write(f'{data} {cfmv} {codigo} {valor} {nome} {nome_vet} 1\n')
        arquivo_dados.close()
        print('=' * 25)
        print('Consulta cadastrada')
        print('=' * 25)


def inativar_consulta(data,cfmv,codigo):
    arquivo = open('consultas.txt', 'r')
    for n in arquivo:
        dados = n.split()
        if len(dados) > 0:
            if dados[0] == data:
                if dados[1] == cfmv:
                    if dados[2] == codigo:
                        consulta = f'{dados[0]} {dados[1]} {dados[2]} 0 {dados[4]} {dados[5]} 2\n'
    try:
        alterar_linha('consultas.txt', data, consulta)
        print('=' * 25)
        print('Consulta suspensa')
        print('=' * 25)
    except:
        print('=' * 25)
        print('Consulta não cadastrada')
        print('=' * 25)


def relatorio_pets():
    print('Relatorio de Pet')
    arquivo = open('dados_animais.txt', 'r')
    for n in arquivo:
        dados = n.split()
        if len(dados) > 0:
            raca = converter_raca(int(dados[2]))
            print(f'Codigo:{dados[0]}---Nome:{dados[1]}----Raça:{raca}')


def relatorio_veterinarios():
    print('Relatorio de veterinários ativos')
    arquivo = open('dados_veterinarios.txt', 'r')
    for n in arquivo:
        dados = n.split()
        if len(dados) > 0:
            if dados[4] == 1:
                sexo = converter_sexo(int(dados[3]))
                print(f'CFMV:{dados[0]}---Nome:{dados[1]}----CPF:{dados[2]}-----Sexo:{sexo}')


def relatorios_consultas(data):
    print('Relatorio de consultas')
    arquivo = open('consultas.txt', 'r')
    valor_total = 0
    for n in arquivo:
        dados = n.split()
        if len(dados) > 0:
            if dados[0] == data:
                    valor_total += int(dados[3])
                    status = converter_status(int(dados[6]))
                    print(f'''=========
Data:{dados[0]}
CFMV:{dados[1]}
Veterinario:{dados[5]}
Codigo de registro do pet:{dados[2]}
Nome do pet:{dados[4]}    
Status:{status}
Valor:R${dados[3]}            
=========''')
    print(f'Nesse dia foi faturado R${valor_total}')