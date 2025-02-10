def verifica_genero(genero):
    while genero != 'M' and genero != "F": #Laço de repetição que se encerra quando genero foi igual a M ou F
        genero = input("Insira M para homem ou F para mulher: ")
        if genero == 'M':
            print("Esta pessoa é um homem.")
        elif genero == "F":
            print("Esta pessoa é uma mulher.")
        else:
            print("Gênero não reconhecido.")

genero = ""
verifica_genero(genero)