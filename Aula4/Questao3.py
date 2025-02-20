import random

import numpy as np

matriz = np.zeros([2,2])
linha = random.randint(0,1) #escolha uma linha, de 0 a 1
coluna = random.randint(0,1) #escolha uma coluna, de 0 a 1

matriz[linha,coluna] = 1 #insera o número 1 na posição escolhida

print("---------------------------------------------------------------------------------------------------------------")
linha_escolha = int(input(f"Seleciona uma linha, de 0 a 1:"))
coluna_escolha = int(input(f"Selecione uma coluna, de 0 a 1:"))

if matriz[linha_escolha,coluna_escolha] != 1:
    print("Congratulations! You beat the game!")
else:
    print("Game over! :( Try again!")