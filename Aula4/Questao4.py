import random

import numpy as np

linhas = random.randint(0,255)
colunas = random.randint(0,255)

matriz = np.random.randint(0,10,[linhas,colunas]) #matriz de tamanho aleatório com números inteiros de 0 a 9

print("---------------------------------------------------------------------------------------------------------------")
print(f"\nNúmero de inhas da matriz: {linhas} ; Número de colunas da matriz: {colunas}.")

tamanho_array = linhas * colunas

print(f"Tamanho do vetor unidimensional: {tamanho_array}")

if tamanho_array % 2 == 0:
    print("Vetor unidimensional com número par de elementos.")
else:
    print("Vetor unidimensional com número ímpar de elementos.")
