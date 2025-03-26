import numpy as np
import pandas as pd

dfPaises = pd.read_csv('paises (1).csv', delimiter = ';')

print(f"-------------------------------------------------------------------------------------------------------------\n")

def paises_da_OCEANIA(dataframe):
    OCEANIA = dataframe.loc[dataframe['Region'] == 'OCEANIA                            ']
    print(f"Países da Oceania: ")
    print(f"{OCEANIA['Country']}")
    print(f"Total de países: {OCEANIA.count()['Country']}")
    print(f"---------------------------------------------------------------------------------------------------------\n")

paises_da_OCEANIA((dfPaises))

def maior_populacao(dataframe):
    mais_populoso = np.max(dfPaises['Population'])
    Pais = dataframe.loc[dataframe['Population'] == mais_populoso]
    print(f'País mais populoso do mundo e sua região:')
    print(f'Nome: {Pais['Country']} , Região: {Pais['Region']}')
    print(f"---------------------------------------------------------------------------------------------------------\n")

maior_populacao(dfPaises)

def media_de_alfabetizacao(dataframe):
    group_by_regions = dataframe.groupby('Region')
    media_alfabetizacao = group_by_regions['Literacy (%)'].mean()
    print(f"Média de alfabetização por região:")
    print(media_alfabetizacao)
    print(f"---------------------------------------------------------------------------------------------------------\n")

media_de_alfabetizacao(dfPaises)

def landlocked(dataframe):
    landlocked_countries = dataframe.loc[dataframe['Coastline (coast/area ratio)'] == 0]
    nomes = landlocked_countries['Country']
    nomes.to_csv('noCoast.csv', sep=';')
    df = pd.read_csv('noCoast.csv', delimiter=';')
    print('Países sem costa:')
    print(df)
    print(f"---------------------------------------------------------------------------------------------------------\n")

landlocked(dfPaises)

def verifica_mortalidade(dataframe):
    def ajuda_humanitaria(x):
        if x < 9:
            x = 'Balanced'
        else: x = 'Urgent'
        return x

    dataframe['Humanitarian Help'] = dataframe['Deathrate'].apply(ajuda_humanitaria)
    print("Situação humanitária em cada país:")
    print(dataframe)

verifica_mortalidade(dfPaises)