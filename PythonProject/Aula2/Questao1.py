#Questão 1
def print_nome(nome): #criando uma função que recebe a variável nome
    # Use a breakpoint in the code line below to debug your script.
    print('Seu nome completo é: ' , nome)  # Print normal
    print('Seu nome com todas as letras maíusculas:' , nome.upper()) # Colocando todas as letras do nome em letra maiúscula
    print('Seu nome com todas as letras minúsculas:', nome.lower()) # Colocando todas as letras do nome em letra minúscula
    print('Número de letras em seu nome: ' , len(nome)) # Descobrindo o número de letras do string nome
    print('Seu novo nome: ' , nome.replace('Reis', 'do Inatel')) #Fazendo uma pequena mudança no meu último nome

nome = input("Insira seu nome completo: ") #criando a variável nome e atribuindo um valor à ela por meio de uma entrada de dados
print_nome(nome) # chamada da função e envio da variável nome