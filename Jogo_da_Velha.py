#Vamos criar 3 funções: uma para mostrar a situação do jogo outra para verificar a vitoria e a ultima para rodar o jogo
# usaremos o join para juntar a matriz que representa o tabuleiro em uma unica string e também para ornamentá-la

def Mostra(matriz):
    for i in matriz:
        print(" | ".join(i))
        print("*" * 9)

#aqui usa a função all() para verificar se tudo naquela linha(que é uma lista) está igual, ou seja, se os valores dessa lista são todos iguais

def Condição_vitoria(matriz, letra):
    for i in range(0,3):
        if all(matriz[i][j] == letra for j in range(0,3)) or all(matriz[j][i] == letra for j in range(0,3)):
            return True
    if all(matriz[i][i] == letra for i in range(0, 3)) or all(matriz[i][2 - i] == letra for i in range(0, 3)):
        return True
    return False

def jogo_principal():
    
    controlador = 1
    matriz = [[' ' for i in range(0, 3)]for j in range(0, 3)]

    while True:

        if controlador > 0:
            letra_jogada = 'X'
        else:
            letra_jogada = 'O'

        Mostra(matriz)

        linha, coluna = map(int,input(f"Jogador {letra_jogada} digite as coordenadas da jogada (Linha, Coluna)").split())
        if matriz[linha-1][coluna-1] != ' ':
            print('Essa coordenada não está vazia')
        else:
            matriz[linha-1][coluna-1] = letra_jogada

            if Condição_vitoria(matriz, letra_jogada) == True:
                Mostra(matriz)
                print(f"Jogador {letra_jogada} ganhou!")
                break
                
            contador = 0
            for i in range(0,3):
                for j in range(0, 3):
                    if matriz[i][j] !=' ' :
                        contador +=1

            if contador == 9 and Condição_vitoria(matriz, letra_jogada) == False:
                Mostra(matriz)
                print("Empate!")
                break
                        
            controlador = controlador * -1
        

    return None



jogo_principal()
