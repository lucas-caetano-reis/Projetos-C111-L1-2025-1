import numpy as np
np.random.seed(10) #plantando semente aleatória para manter o resultado em qualquer dispositivo
matriz = np.random.randint(1,51,[4,4])

print("---------------------------------------------------------------------------------------------------------------")
print(f"Matriz:\n{matriz}\n")

media_linhas = matriz.mean(axis = 0) #média das linhas
media_colunas = matriz.mean(axis = 1) #média das colunas

max_media_linhas = media_linhas.max()
max_media_colunas = media_colunas.max()

#encontra cada elemento e faz a contagem da frequência de aparição
valores, contagem = np.unique(matriz, return_counts=True)

#função que encontra os elementos repetidos
def encontrar_elementos_repetidos(matriz):
    valores, contagem = np.unique(matriz, return_counts=True)
    return valores[contagem == 2]

elementos_repetidos = encontrar_elementos_repetidos(matriz)


print(f"Média dos valores de cada linha: {media_linhas}")
print(f"Média dos valores de cada coluna: {media_colunas}")
print(f"Maior valor das médias das linhas: {max_media_linhas}")
print(f"Maior valor das médias das colunas: {max_media_colunas}")
print(f"Frequência de aparição de cada elemento único:{valores};\n{contagem}")
print(f"Elementos que aparecem duas vezes na array: {elementos_repetidos}")
