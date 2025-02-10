#Questão 2
def tabuada(numero, intervalo):
    for numeros in range(0 , intervalo): #laço de repetição de 0 até intervalo - 1
        numero += 1
        print(numero)

numero = int(input("Insira um número à sua escolha: "))
intervalo = int(input("Insira um intervalo à sua escolha: "))
tabuada(numero,intervalo)