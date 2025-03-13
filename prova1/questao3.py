import numpy as np

dataset = np.loadtxt('social_media.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

def views_likes_instagram(dataset):
    eh_do_instagram = dataset[1:][dataset[1: , 1] == "Instagram"] #filtra as células para guardar apenas os posts feitos no Instagram
    views = eh_do_instagram[1: , 5].astype(float)
    likes = eh_do_instagram[1:, 6].astype(float)
    media_de_views = round(views.mean() , 4)
    media_de_likes = round(likes.mean() , 4)

    dicionario = {'Media de views' : media_de_views , 'Média de likes' : media_de_likes}

    print(dicionario.items())

views_likes_instagram(dataset)
