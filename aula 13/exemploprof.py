from bs4 import BeautifulSoup
import requests


url = 'https://gratuitos.netlify.app/'

requ = requests.get(url)
site = BeautifulSoup(requ.text, 'html.parser')
print(site)
dados =  site.find('table', class_='table table-sm bg-light text-left', scope_='col')
print(dados)

