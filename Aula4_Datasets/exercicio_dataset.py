import numpy as np
dataset = np.loadtxt('space.csv', delimiter=";", dtype=str, encoding='utf-8') #carrega o dataset

print("---------------------------------------------------------------------------------------------------------------")

#questão 1
def porcentagem_de_sucesso(dataset):
    sucesso = np.count_nonzero(dataset[1 : , 7] == "Success") #Ocorrências de Success
    tamanho = dataset.shape[0] - 1 #calcula o número de linhas menos o cabeçalho

    porcentagem = round((sucesso / tamanho) * 100, 4)  # encontra a porcentagem de sucesso das missões e a arredonda para 4 casas decimais

    return porcentagem

print(f"Porcentagem de missões realizadas com sucesso: {porcentagem_de_sucesso(dataset)}\n")

print("---------------------------------------------------------------------------------------------------------------")

#Questão 2
def media_de_custo(dataset):
    custos = dataset[1 : , 6].astype(float) #muda a variável da coluna de custos das missões, de string para float
    custos_disponiveis = custos[custos > 0] #filtra a coluna de custos, onde o valor de custos é maior que 0
    media = round(np.mean(custos_disponiveis), 4) #calcula a média, com 4 casas decimais

    return media

print(f"Média de custo das missões realizadas: {media_de_custo(dataset)}\n")

print("---------------------------------------------------------------------------------------------------------------")

#Questão 3
def realizada_pelos_EUA(dataset):
    array_EUA = dataset[(np.char.find(dataset, 'USA') > 0)] #filtra as células que fazem menção aos EUA
    missoes_americanas = array_EUA.shape[0] #encontra o tamanho da array auxiliar, e consequentemente o número de missões americanas
    return missoes_americanas


print(f"Número de missões realizadas pelos EUA: {realizada_pelos_EUA(dataset)}\n")

print("---------------------------------------------------------------------------------------------------------------")

#Questão 4
def missao_mais_cara_da_SpaceX(dataset):
    Eh_da_SpaceX = dataset[1:][dataset[1 : , 1] == "SpaceX"] #Missões feitas pelas Space X. Usei duas máscaras booleanas
    #uma que pega todas as linhas a partir da 1
    #outra que filtra as linhas para deixar apenas aquelas onde SpaceX está na coluna 1
    custos = Eh_da_SpaceX[:, 6].astype(float)  # muda a variável da coluna de custos das missões da SpaceX, de string para float
    indice_da_missao_mais_cara = custos.argmax() #pega o índice da missão mais cara da SpaceX
    return Eh_da_SpaceX[indice_da_missao_mais_cara] #mostra todos os detalhes da missão mais cara da SpaceX

print(f"Missão mais cara realizada pela SpaceX: {missao_mais_cara_da_SpaceX(dataset)}\n")

print("---------------------------------------------------------------------------------------------------------------")

#Questão 5
def empresas_que_ja_fizeram_missoes(dataset):
    companhias, quantidade = np.unique(dataset[1:, 1], return_counts=True) #filtra as companhias, excluindo as repetições
    #e conta a quantidade de aparições de cada uma
    return dict(zip(companhias, quantidade)) #cria um dicionário, unindo as variáveis companhias e quantidade para facilitar o coding
    #e a vizualização dos dados

missoes_por_empresa = empresas_que_ja_fizeram_missoes(dataset) #chama a função e recebe o dicionário
print("Número de missões por companhia:")
for empresa, quantidade_de_missoes in missoes_por_empresa.items(): #roda o dicionário
    print(f"{empresa}: {quantidade_de_missoes}") #mostra o nome da empresa e seu número de missões

print("---------------------------------------------------------------------------------------------------------------")
