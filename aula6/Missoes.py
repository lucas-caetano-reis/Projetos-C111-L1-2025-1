import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Lê o dataset
dfspace = pd.read_csv('dataframes/space.csv', delimiter=';')

# Filtra as missões que foram realizadas em localidades nos EUA ou China
paises = dfspace[dfspace['Location'].str.contains('USA|China')]

# Conta quantas empresas espaciais existem neste países
empresas_por_pais = paises.groupby(paises['Location'].str.extract(r'(USA|China)')[0])['Company Name'].nunique()
#extrai as expressões regulares USA e China
#cria um novo dataframe de apenas uma coluna contendo apenas os nomes destes dois países
#agrupa o dataframe por localidade
#conta quantas empresas diferentes existem em cada grupo

plt.bar(empresas_por_pais.index, empresas_por_pais.values, color=['red', 'blue'])

plt.xlabel('País')
plt.ylabel('Número de Empresas Espaciais')
plt.title('Quantidade de Empresas Espaciais nos EUA e na China')

plt.show()