import requests
from bs4 import BeautifulSoup

url = 'https://gratuitos.netlify.app'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

titulo = soup.title.string
print("Título da página:", titulo)