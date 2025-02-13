loja1 = {'iPhone 16', 'Samsung Galaxy Explosivo', 'Xiaomi 1984', 'Nokia Tijolão'} #conjunto {}
loja2 = {'Moto X4 relíquia', 'LG que ninguém lembra', 'Nokia Tijolão', 'Xiaomi 1984'}

print(f'\n{loja1}')
print(f'{loja2}\n')

total = loja1 | loja2 #união
print(f'{total}\n')
comum = loja1 & loja2 #interseção
print(f'{comum}')