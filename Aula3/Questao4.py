pessoa1 = {'nome': 'Pedro', 'peso': 85.0}
pessoa2 = {'nome': 'João', 'peso': 80.4}
pessoa3 = {'nome': 'Oswaldo', 'peso': 100.5}
pessoas = [pessoa1, pessoa2, pessoa3]

menor = pessoas[0]['peso']
maior = pessoas[0]['peso']

# Encontrar os valores mínimo e máximo de peso
for pessoa in pessoas:
    if pessoa['peso'] < menor:
        menor = pessoa['peso']
    if pessoa['peso'] > maior:
        maior = pessoa['peso']

# Exibir as pessoas com menor e maior peso
for pessoa in pessoas:
    if pessoa['peso'] == menor:
        print(f"Pessoa com menor peso: {pessoa['nome']} - {pessoa['peso']}")
    if pessoa['peso'] == maior:
        print(f"Pessoa com maior peso: {pessoa['nome']} - {pessoa['peso']}")