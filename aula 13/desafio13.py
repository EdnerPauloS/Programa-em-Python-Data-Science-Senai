# ATIVIDADE 1
# GERAR GRAFICO LEVANTAMENTO DE DADOS


# Buscar todas as idades 

from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt  
import pandas as pd
import tkinter as tk


url = 'https://tabelatest.netlify.app/'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')
dados = soup.find('tbody').get_text()
# print(dados)

nome = []
idade = []
cidade = []
email = []

dado in soup.find_all('tbody'):
nome=[dado.find('td')]
idade.append(dado.find('td'[1]))
    # cidade.append(dado.find('td'[2]))
    # email.append(dado.find('td'[3]))

# print(nome)
# print(idade)
# print(soup)

df  = pd.DataFrame({
    'Nome':nome,
    'idade':idade,
    'cidade':cidade,
    'email': email
})
df=pd.DataFrame(df)
print(df)

df.to_csv('tabela1.csv', index=False)

df  =  pd.read_csv('tabela1.csv')