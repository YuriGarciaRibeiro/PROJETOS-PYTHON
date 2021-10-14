def alterar_linha(path,codigo,nova_linha):
    with open(path,'r') as f:
        texto=f.readlines()
    with open(path,'w') as f:
        for i in texto:
            if codigo in i:
                f.write(nova_linha+'\n')
            else:
                f.write(i)





def cadastrar_clientes(nome,cpf):
    arquivo_dados = open('dados_pessoas.txt', 'r')
    cont = 0
    for linha in arquivo_dados:
        dados = linha.split()
        if len(dados) > 0:
            if int(dados[1]) == (cpf):
                cont += 1
    arquivo_dados.close()
    if cont == 1:
        print('CPF já cadastrado')
    else:
        arquivo_dados = open('dados_pessoas.txt', 'a')
        arquivo_dados.write(f'{nome} {cpf}\n')
        arquivo_dados.close()
def cadastrar_maquina(codigo,tipo,marca,modelo,ano,valor,status):
    contador = 0
    arquivo_dados = open('dados_maquinas.txt','r')
    for linha in arquivo_dados:
        dados = linha.split()
        contador += 1
        if contador == 3:
            break
    arquivo_dados.close()
    if contador < 3:
        arquivo_dados = open('dados_maquinas.txt','a')
        arquivo_dados.write(f'{codigo} {tipo} {marca} {modelo} {ano} {valor} {status}\n')
    else:
        print('O limite de máquinas já foi atingido')
            
def reservar_maquina(cpf,codigo):
    try:
        arquivo = open('dados_pessoas.txt','r')
        for n in arquivo:
            dados = n.split()
            try:
                if int(dados[1]) == int(cpf):
                    nome = dados[0]
            except:
                pass
        arquivo = open('dados_maquinas.txt', 'r')
        for n in arquivo:
            dados = n.split()
            try:
                if int(dados[6]) == 1:
                    if int(dados[0]) == int(codigo):
                        maquina = f'{dados[0]} {dados[1]} {dados[2]} {dados[3]} {dados[4]} {dados[5]} 2'
            except:
                pass
        alterar_linha('dados_maquinas.txt',codigo,f'{maquina} {nome}\n')
    except :
        print('Máquina já está reservada')

def relatorio_clientes():
    print('Relatorio de Clientes')
    arquivo = open('dados_pessoas.txt', 'r')
    for n in arquivo:
        dados = n.split()
        print(f'Nome:{dados[0]}---CPF:{dados[1]}')
def relatorio_maquinas():
    print('Relatório de máquinas')
    arquivo = open('dados_maquinas.txt', 'r')
    for n in arquivo:
        dados = n.split()
        try:
            if int(dados[1]) == 1:
                tipo = 'Perfurador'
            elif int(dados[1]) == 2:
                tipo = 'Demolidor'
            elif int(dados[2]) == 3:
                tipo = 'Compactador'
            if int(dados[6]) == 1:
                status = 'Disponivel'
            if int(dados[6]) == 2:
                status = 'Indisponivel'
        except:
            pass


        try:

            print(f'''========
Código:{dados[0]}
Tipo:{tipo}
Marca:{dados[2]}
Modelo:{dados[3]}
Ano:{dados[4]}
Valor do Aluguel:{dados[5]}        
Status:{status} 
========''')
        except:
            pass

def relatorios_reservas():




    print('Relatório de reservas')
    arquivo = open('dados_maquinas.txt', 'r')
    for n in arquivo:
        dados = n.split()
        try:
            if int(dados[1]) == 1:
                tipo = 'Perfurador'
            elif int(dados[1]) == 2:
                tipo = 'Demolidor'
            elif int(dados[2]) == 3:
                tipo = 'Compactador'
        except :
            pass
        try:
            print(f'Nome:{dados[7]}-----Código:{dados[0]}----Tipo:{tipo}----Valor:R${dados[5]}')
        except:
            pass