import numpy as np

dataset = np.loadtxt('social_media.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

def encontrar_posts_brasileiros(dataset):
    eh_do_brasil = np.count_nonzero(dataset[1 : , 4] == "Brazil")
    return eh_do_brasil

print(f"Número de posts realizados no Brasil: {encontrar_posts_brasileiros(dataset)}\n")
