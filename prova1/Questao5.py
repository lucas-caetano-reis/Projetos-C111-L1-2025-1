import numpy as np

dataset = np.loadtxt('social_media.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

def encontrar_regiao_com_o_melhor_post(dataset):
    likes = dataset[1: , 6].astype(int)
    maior_numero_de_likes = likes.max()


    print(f"Maior número de likes em um só post: {maior_numero_de_likes}")

encontrar_regiao_com_o_melhor_post(dataset)

#o resto eu não consegui fazer