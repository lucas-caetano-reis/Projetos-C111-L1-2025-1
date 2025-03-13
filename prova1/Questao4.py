import numpy as np

dataset = np.loadtxt('social_media.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

def plataforma_com_mais_posts(dataset):
    plataforma , frequencia = np.unique(dataset[1: , 1], return_counts= True)
    dicionario = dict(zip(plataforma, frequencia))

    print(f"Dicionário com cada plataforma e seus itens: \n")
    print(dicionario.items())

plataforma_com_mais_posts(dataset)

#sumiu da minha memória a maneira correta de terminar esse código
