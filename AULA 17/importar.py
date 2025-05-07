import tkinter as tk
from bs4 import BeautifulSoup
import pandas as pd
import requests

url = 'https://tabelatest.netlify.app/'
resposta = requests.get(url).text
soup = BeautifulSoup(resposta, 'html.parser')

idade  = [linha.find_all('td')[1].text for linha in soup.find_all('tr')[1:]]

idades = [int(i) for i in idade ]

cidade = [linha.find_all('td')[2].text for linha in soup.find_all('tr')[1:]]

e_mails = [linha.find_all('td')[3].text for linha in soup.find_all('tr')[1:]]

nomes =  [linha.find_all('td')[0].text for linha in soup.find_all('tr')[1:]]

def mostrar():
    organizacao_dados = ({
    'idades':idades,
    'cidades':cidade,
    'nomes': nomes,
    'e-mail':e_mails
})
    df = pd.DataFrame(organizacao_dados)
    df.to_excel('dados.xlsx', index=False)
    dados = pd.read_excel('dados.xlsx')
    dados_mostrados.config(text=dados)

root =  tk.Tk()

btn = tk.Button(root, text='carregue', command=mostrar)
btn.pack()

dados_mostrados = tk.Label(root, text='')
dados_mostrados.pack()

root.mainloop()