from bs4 import BeautifulSoup
import requests

# URL do site
url = 'https://gratuitos.netlify.app/'

# Requisição para obter o conteúdo da página
requ = requests.get(url)
site = BeautifulSoup(requ.text, 'html.parser')

# Vamos buscar a tabela por uma classe mais genérica
# Aqui estamos usando 'table-responsive' e 'table' como referências, mas podemos adicionar outras classes se necessário
tabela = site.find('table', class_='table')  # Tentamos encontrar uma tabela com a classe 'table'

# Verificação se a tabela foi encontrada
if tabela:
    # Encontrar todas as linhas da tabela (tr)
    linhas = tabela.find_all('tr')
    
    # Criar uma lista para armazenar os dados da tabela
    dados_tabela = []

    # Iterar sobre cada linha
    for i, linha in enumerate(linhas):
        # Buscar as células da linha (pode ser th ou td)
        colunas = linha.find_all(['th', 'td'])
        
        # Se houver dados nas colunas, vamos extraí-los
        if colunas:
            dados_linha = [coluna.get_text(strip=True) for coluna in colunas]
            
            # Exibir o índice da linha e os dados extraídos
            print(f"Linha {i + 1}: {dados_linha}")
            
            # Adicionar os dados extraídos à lista de dados da tabela
            dados_tabela.append(dados_linha)

    # Se a tabela for encontrada, também podemos retornar os dados extraídos em um formato organizado
    if dados_tabela:
        print("\nDados da Tabela Extraídos com Sucesso:")
        for linha in dados_tabela:
            print(linha)

else:
    print("Tabela não encontrada na página.")
