import numpy as np

array1 = np.arange(0, 52, 2) #pula de 2 em 2
array2 = np.arange(100, 49, -2) #o mesmo, só que de forma decrescente

print("---------------------------------------------------------------------------------------------------------------")
print(f"\nArray de valores pares, de 0 até 51:\n{array1}\n")
print(f"Array de valores pares, de 100 até 50:\n{array2}\n")

array_concatenado = np.concatenate((array1, array2))
array_resultante = np.sort(array_concatenado)

print(f"Array resultante:\n{array_resultante}")