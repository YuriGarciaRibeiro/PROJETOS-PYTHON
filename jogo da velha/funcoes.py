def gerar_vitorias(nome_arquivo):
    vitorias = []
    arquivo = open(f'{nome_arquivo}.txt', 'r')
    for n in arquivo:
        vitorias.append([])
        for c in n:
            if c.isnumeric() == True:
                vitorias[len(vitorias) - 1].append(int(c))
    return vitorias


def consultar_vitoria(matriz, jogo):
    pontos_X = 0  # 1
    pontos_0 = 0  # 2
    for n in range(len(matriz)):
        if pontos_X < 3:
            if pontos_0 < 3:
                pontos_X = 0  # 1
                pontos_0 = 0  # 2
                for c in range(len(matriz[n])):
                    if pontos_X < 3:
                        if pontos_0 < 3:
                            if matriz[n][c] == 1 and jogo[c] == 'X':
                                pontos_X += 1

                            if matriz[n][c] == 2 and jogo[c] == '0':
                                pontos_0 += 1
                        else:
                            break
                    else:
                        break
            else:
                break
        else:
            break
    if pontos_0 == 3:
        return 2
    elif pontos_X == 3:
        return 1