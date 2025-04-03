import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfpaises = pd.read_csv('dataframes/paises.csv', delimiter=';') #lendo o dataframe de países
dfpaises2 = dfpaises[dfpaises['Region'] == 'NORTHERN AMERICA                   '] #filtrando os países da América do Norte

dfNorthernAmerica = dfpaises2['Country'] #pegando os países da América do Norte
dfDeathrate = dfpaises2['Deathrate']#pegando suas taxas de mortalidade
dfBirthrate = dfpaises2['Birthrate'] #pegando suas taxas de natalidade

plt.figure(figsize=(10, 5))
plt.xlabel('Países')
plt.ylabel('Mortalidade (Vermelho) , Natalidade (Azul')
plt.title('Taxas (%) de Mortalidade e Natalidade na América do Norte')

plt.plot(dfNorthernAmerica, dfDeathrate,'r--s', dfNorthernAmerica, dfBirthrate, 'b:p')
plt.grid(True)
plt.show()