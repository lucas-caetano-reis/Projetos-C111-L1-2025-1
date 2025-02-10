def ler_numero(numero):
    numero_str = str(numero)
    print("Numero da unidade: " , numero_str[3])
    print("Numero da dezena: " , numero_str[2])
    print("Numero da centena: " , numero_str[1])
    print("Numero do milhar: " , numero_str[0])

numero = 0
while not 1000 <= numero <= 9999:
    numero = int(input("Insira um número de 1000 a 9999: "))
ler_numero(numero)