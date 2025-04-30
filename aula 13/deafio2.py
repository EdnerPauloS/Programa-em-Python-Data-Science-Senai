import requests
from bs4 import BeautifulSoup

url = 'https://gratuitos.netlify.app'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Supondo que a tabela tenha a tag <table>
tabela = soup.find('table')

if tabela:
    linhas = tabela.find_all('tr')
    for linha in linhas:
        colunas = linha.find_all(['th', 'td'])
        dados = [coluna.get_text(strip=True) for coluna in colunas]
        print(dados)
else:
    print("Tabela não encontrada.")