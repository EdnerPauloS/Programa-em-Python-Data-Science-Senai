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

tbody = soup.find('tbody')

for linha in tbody.find_all('tr'):
    colunas = linha.find_all('td')
    if len (colunas)>=4:
        nome.append(colunas[0].get_text(strip=True))
        idade.append(int(colunas[1].get_text(strip=True)))
        cidade.append(colunas[2].get_text(strip=True))
        email.append(colunas[3].get_text(strip=True))

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

# print(df)

df.to_csv('tabela1.csv', index=False)

df  =  pd.read_csv('tabela1.csv')

print(df.describe())
print(df.info())
print(df.head())

idade_media = df.groupby('cidade')['idade'].mean().sort_values(ascending=False)
idade_mediana = df.groupby('cidade')['idade'].median().sort_values(ascending=False)
nomes_media = df.groupby('Nome')['idade'].mean().sort_values(ascending=False)
nomes_mediana = df.groupby('Nome')['idade'].median().sort_values(ascending=False)
email_media = df.groupby('email')['idade'].mean().sort_values(ascending=False)
email_mediana = df.groupby('email')['idade'].median().sort_values(ascending=False)

print(idade_media)
print(idade_mediana)
print(nomes_media)
print(nomes_mediana)
print(email_media)
print(email_mediana)



plt.figure(figsize=(10,6))
plt.hist(df['idade'], bins=range(min(df['idade']), max(df['idade'])+1), edgecolor='black')
plt.title('Distribuição de Idade')
plt.xlabel('Idade')
plt.ylabel('Frequência')
plt.grid(True)
plt.show()


plt.figure(figsize=(10,6))
idade_media.plot(kind='bar', color='red')
plt.title('Média de Idade por Cidade')
plt.xlabel('Cidade')
plt.ylabel('Idade Média')
plt.grid(True)
plt.xticks(rotation=45)
plt.show()

df['Tamanho_Nome'] = df['Nome'].apply(len)

plt.figure(figsize=(10,6))
plt.scatter(df['idade'], df['Tamanho_Nome'], color='green')
plt.title('Relação entre Idade e Tamanho do Nome')
plt.xlabel('Idade')
plt.ylabel('Tamanho do Nome (caracteres)')
plt.grid()
plt.show()

df.to_csv('dados_extraidos.csv', index=False)
