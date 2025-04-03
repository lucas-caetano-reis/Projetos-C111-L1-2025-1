import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dfspace = pd.read_csv('dataframes/space.csv', delimiter=';') #lendo o dataframe de missões espaciais

dfspace2 = dfspace[dfspace['Company Name'] == 'Roscosmos'] #filtra todas as missões feitas pela Roscosmos
sucesso = len(dfspace2[dfspace2['Status Mission'] == 'Success']) #calcula o número de missões da Roscosmos que deram certo
fracasso = len(dfspace2[dfspace2['Status Mission'] == 'Failure']) #calcula o resto

plt.pie(x=[sucesso,fracasso], labels=['% Sucesso' , '% Fracasso'], autopct='%1.1f%%')
plt.show()