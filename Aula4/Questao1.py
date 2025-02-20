import numpy as np
#criando duas arrays unidimensional de 8 dimensões
array1 = np.ones(8) #formada apenas por 1's
array2 = np.random.randint(0,10,8) #array com valores aleatórios de 0 a 9

print("---------------------------------------------------------------------------------------------------------------")
print(f"Array de 1's: {array1}\n")
print(f"Array de números aleatórios: {array2}\n")

#criando uma array que armazena a soma das duas arrays a cima
array_soma = array1 + array2
print(f"Array resultante: {array_soma}\n")

print("---------------------------------------------------------------------------------------------------------------")
#Operações com a array resultante
#Caso a soma dos elementos da array seja >= 40
if array_soma.sum() >= 40:
    mtz = array_soma.reshape(4 , 2)
    print(f"Matriz com mais linhas do que colunas:\n{mtz}")
else:
    mtz = array_soma.reshape(2, 4)
    print(f"Matriz com mais colunas do que linhas:\n{mtz}")