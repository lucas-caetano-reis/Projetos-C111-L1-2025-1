import numpy as np

dataset = np.loadtxt('social_media.csv', delimiter = ';', dtype = str, encoding = 'utf-8')

def porcentagem_education(dataset):
    education = np.count_nonzero(dataset[1 : , 2] == "Education")
    tamanho = np.size(dataset, 0) - 1 #excluindo o cabeçalho
    porcentagem = round((education / tamanho) * 100 , 4)
    return porcentagem

print(f"Porcentagem de posts com a hashtag 'Education': {porcentagem_education(dataset)}\n")