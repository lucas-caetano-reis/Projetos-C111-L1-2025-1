import math

def resultados(numero):
    print("Raiz quadrada: " , math.sqrt(numero))
    print("Função teto: ", math.ceil(numero))
    print("Função chão: ", math.floor(numero))
    print("Valor inteiro: ", numero // 1)


numero = float(input("Insira um número decimal: "))

resultados(numero)