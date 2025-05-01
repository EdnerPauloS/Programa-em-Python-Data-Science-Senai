import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Qual a estimativa de quantidade de mortes por continente?
# Qual a estimativa de de testes por continente?  



# Utilizando fillna()

dados = pd.read_csv('covid_19.csv')

pais = dados['country'].str.replace(',,',',não tem,').to_list()
continente = dados['continent'].fillna('outros').to_list()
mortes = dados['Deaths'].fillna(0).astype(float).to_list()

n_mortes = mortes[0:20]
n_continente=continente[0:20]

print(n_mortes)
print(n_continente)