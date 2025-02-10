def calcula_preco(km):
    if km <= 200:
        preco = 0.50 * km
    else:
        preco = 0.45 * km

    print("Preço da passagem: " , preco)

km = int(input("Insira a distância da viagem em kilômetros: "))
preco = ""
calcula_preco(km)