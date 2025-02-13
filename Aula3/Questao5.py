n = int(input(f'Entre com o número de pessoas:'))
pessoas = []
for i in range(0,n):
    pessoa = {'nome': '', 'idade': '', 'sexo': ''}
    print(f'\nEntre com os dados da pessoa {i + 1}:')
    pessoa['nome'] = input('Nome da pessoa: ')
    pessoa['idade'] = int(input('Idade da pessoa: '))
    pessoa['sexo'] = input('Sexo da pessoa: ')
    pessoas.append(pessoa)

soma = 0
menor_que_20 = 0
for alguem in pessoas:
    soma += alguem['idade']

    if alguem['sexo'] == "F":
        if alguem['idade'] < 20:
            menor_que_20 += 1

media_de_idade = soma / len(pessoas)
print(f"\nMédia de idade do grupo: {media_de_idade}")
print(f"Número de mulheres com menos de 20 anos: {menor_que_20}")