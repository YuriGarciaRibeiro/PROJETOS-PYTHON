import os

from random import choice
from funcoes import *


jogo = ['1','2','3','4','5','6','7','8','9']#jogo imaginario



vitorias = gerar_vitorias('vitorias')   
x = consultar_vitoria(vitorias,jogo)
casas = [0,1,2,3,4,5,6,7,8]

icone = str(input('escolha qual voce quer usar [0/X]: ')).upper()
if icone == 'X':
    icone_bot = '0'
if icone == '0':
    icone_bot = 'X'


for n in range(0,5):
    os.system('cls')
    print(f'''            [{jogo[0]}] [{jogo[1]}] [{jogo[2]}]
            [{jogo[3]}] [{jogo[4]}] [{jogo[5]}]
            [{jogo[6]}] [{jogo[7]}] [{jogo[8]}]''')
    escolha = int(input('digite qual lugar voce quer escolher: '))
    jogo[escolha-1] = str(icone)
    casas.remove(int(escolha)-1)
    if len(casas) > 0:
        escolha_bot = choice(casas)
        jogo[escolha_bot] = str(icone_bot)
        casas.remove(escolha_bot)
    x = consultar_vitoria(vitorias,jogo)
    if x == 1:
        os.system('cls')
        print(f'''            [{jogo[0]}] [{jogo[1]}] [{jogo[2]}]
            [{jogo[3]}] [{jogo[4]}] [{jogo[5]}]
            [{jogo[6]}] [{jogo[7]}] [{jogo[8]}]''')
        print('X ganhou')
        break
    if x == 2:
        os.system('cls')
        print(f'''            [{jogo[0]}] [{jogo[1]}] [{jogo[2]}]
            [{jogo[3]}] [{jogo[4]}] [{jogo[5]}]
            [{jogo[6]}] [{jogo[7]}] [{jogo[8]}]''')
        print('bola ganhou')
        break