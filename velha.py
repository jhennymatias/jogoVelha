"""
    Autor: Jhennifer Cristine Matias
    Projeto: Jogo da velha multiplayer
    X = 1
    o = -1
    tabuleiro = matriz[3][3]
"""
import sys
tabuleiro = [[0,0,0], [0,0,0], [0,0,0]]


def valida(x,y):
    """
       A função serve para verificar
       se a posição já foi ocupada
    """
    if tabuleiro[x][y] != 0:
        return -1

def posicao(jogador):
    """
    O usuário escolha onde quer jogar
    e é alterado o tabuleiro
    """
    print("1 2 3")
    print("4 5 6")
    print("7 8 9")
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        x = 0
        y = 0
    elif opcao == 2:
        x = 0
        y = 1
    elif opcao == 3:
        x = 0
        y = 2
    elif opcao == 4:
        x = 1
        y = 0
    elif opcao == 5:
        x = 1
        y = 1
    elif opcao == 6:
        x = 1
        y = 2
    elif opcao == 7:
        x = 2
        y = 0
    elif opcao == 8:
        x = 2
        y = 1
    elif opcao == 9:
        x = 2
        y = 2
    else:
        print("Inválido!")
        posicao(jogador)

    if valida(x,y) == -1:
        print("Posição inválida!")
        posicao(jogador)
    else:
        tabuleiro[x][y] = int(jogador)

def ganhou():
    """
    Verifica se o jogador ganhou, para ganhar a soma tem que ser 3
    na diagonal ou vertical ou horizontal
    """
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == 1:
                print(str("X") + " ", end="")
            elif tabuleiro[i][j] == -1:
                print(str("O") + " ", end="")
            else:
                print("  ", end="")
        print("")

    soma_diagonal = 0
    for i in range(3):
        soma = 0
        soma2=0
        for j in range(3):
            soma = soma + tabuleiro[i][j]
            soma2 = soma2 + tabuleiro[j][i]
            if i == j:
                soma_diagonal = soma_diagonal + tabuleiro[i][j]

        if soma == -3 or soma2 == -3:
            print("Jogador 1 ganhou!")
            sys.exit()
        elif soma == 3 or soma2 ==3:
            print("Jogador 2 ganhou!")
            sys.exit()
        elif soma_diagonal == -3:
            print("Jogador 1 ganhou!")
            sys.exit()
        elif soma_diagonal == 3:
             print("Jogador 2 ganhou!")
             sys.exit()

        if tabuleiro[0][2] == -1 and tabuleiro[1][1] == -1 and tabuleiro[2][0] == -1:
            print("Jogador 1 ganhou!")
            sys.exit()

        if tabuleiro[0][2] == 1 and tabuleiro[1][1] == 1 and tabuleiro[2][0] == 1:
            print("Jogador 2 ganhou!")
            sys.exit()

print("=============== Jogo da velha ================= ")
print("O jogador O é o jogador 1")
print("O jogador X é o jogador 2 \n")
print("Para jogar basta escolher uma posição de 1 a 9 ainda não preenchida. \n ")

while 1:
    posicao(1)
    ganhou()
    posicao(-1)
    ganhou()

