import pandas as pd
import numpy as np

# Questão 6

np.random.seed(10)
df = pd.DataFrame(
    index = ['A', 'B', 'C', 'D', 'E'],
    columns = ['W', 'X', 'Y', 'Z'],
    data = np.random.randint(1, 50, [5,4])
)

print(f"Dataframe utilizado:")
print(f"{df}\n")

media_X_maior_que_30 = np.mean(df['X'][df['X'] > 30]) #Pega a coluna X, faz a filtragem de dados e encontra a média

print(f"Média dos elementos da coluna X que são maiores do que 30: {media_X_maior_que_30}\n")

# Questão 7

linhaD = df.loc[['D'],['W', 'X', 'Y', 'Z']]
linhaE = df.iloc[4 , :]

print(f"Linha D:")
print(f"{linhaD}")
print(f"Média: {np.mean(linhaD)}\n")

print(f"Linha E:")
print(f"{linhaE}")
print(f"Soma: {np.sum(linhaE)}\n")

# Questão 8

slicing = df.loc[['A', 'C', 'E'],['X', 'Y']]
print(f"Dataframe após o slicing:")
print(f"{slicing}\n")

somaA = np.sum(slicing.loc['A' , :])
somaC = np.sum(slicing.loc['C' , :])
somaE = np.sum(slicing.loc['E' , :])
somaX = np.sum(slicing.loc[: , 'X'])
somaY = np.sum(slicing.loc[: , 'Y'])

print(f"Soma da linha A: {somaA}")
print(f"Soma da linha C: {somaC}")
print(f"Soma da linha E: {somaE}")
print(f"Soma da coluna X: {somaX}")
print(f"Soma da coluna Y: {somaY}")