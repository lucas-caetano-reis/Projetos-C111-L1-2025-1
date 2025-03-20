import pandas as pd
import numpy as np

#Questão 1

seriesAno1 = pd.Series({'Java': 16.25, 'C': 16.04, 'Python': 9.85})
seriesAno2 = pd.Series({'C': 16.21, 'Python': 12.12, 'Java': 11.68})

print(f"Valores de mercado do ano 1:")
print(f"{seriesAno1}\n")
print(f"Valores de mercado do ano 2:")
print(f"{seriesAno2}\n")

#Questão2

fatia1 = np.sum(seriesAno1)
fatia2 = np.sum(seriesAno2)

print(f"Porcentagem total das fatias de mercado no ano 1: {fatia1}")
print(f"Porcentagem total das fatias de mercado no ano 2: {fatia2}\n")

#Questão 3

saldo = (seriesAno2 - seriesAno1)
print(f"Saldo de fatias de mercado das linguagens entre o ano 1 e o ano 2:")
print(f"{saldo}\n")

#Questão 4

crescimento = saldo[saldo > 0]

print(f"Linguagens que tiveram crescimento:")
print(f"{crescimento}\n")

#Questão 5

print(f"Simulando o crescimento e declínio durante 2 anos, com as mesmas taxas:")
saldo_ano4 = saldo * 3 #saldo do ano 2, mais saldo do ano 3, mais saldo do ano 4
print(f"Saldo de fatias de mercado no ano 4:")
print(f"{saldo_ano4}\n")

fatias_finais = seriesAno1 + saldo_ano4

print(f"Fatias de mercado no ano 4:")
print(f"{fatias_finais}\n")
print(f"Linguagem mais popular ao fim do ano 4: {fatias_finais.nlargest(1)}")