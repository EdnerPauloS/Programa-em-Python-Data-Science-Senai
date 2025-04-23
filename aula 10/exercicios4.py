import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_agg import FigureCanvasAgg


# Atividade Prática: Visualização de Dados com Matplotlib
def vendas():
    # Lê o arquivo CSV
    df = pd.read_csv('novo.csv')
    print(df.describe())
    print(df.head())



    # 1. Gráfico de Pizza: Mostre a distribuição de vendas por mês.
    plt.figure(figsize=(12,10))
    plt.subplot(221)
    plt.pie(df['Vendas'], labels=df['Mês'], autopct='%1.1f%%')
    plt.title('Distribuição de Vendas por Mês')


    # # 2. Gráfico de Dispersão: Relacione vendas e lucro.
    plt.subplot(222)
    plt.scatter(df['Vendas'], df['Lucro'], color='green')
    plt.title('Vendas x Lucro')
    plt.xlabel('Vendas')
    plt.ylabel('Lucro')
   

    # # 3. Gráfico de Barras: Compare vendas por mês.
    plt.subplot(223)
    plt.bar(df['Mês'], df['Vendas'], color='skyblue')
    plt.title('Vendas por Mês')
    plt.xlabel('Mês')
    plt.ylabel('Vendas')


    # # 4. Gráfico de Linha: Mostre a evolução do lucro ao longo dos meses.
    plt.subplot(224)
    plt.plot(df['Mês'], df['Lucro'], marker='o', color='red')
    plt.title('Lucro ao Longo dos Meses')
    plt.xlabel('Mês')
    plt.ylabel('Lucro')
    plt.show()

vendas()
