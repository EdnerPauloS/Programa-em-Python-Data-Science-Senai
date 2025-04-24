import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk

dados = pd.read_csv('desafiodados.csv')


df = pd.DataFrame(dados)
df.sorted = df.sort_values(by='vendedor') # Ordenando por vendedor para melhor visualização (opcional)
vendedores = df.sorted['vendedor'].unique()
vendas_por_vendedor = {}
for vendedor in vendedores:
    vendas_por_vendedor[vendedor] = df.sorted[df.sorted['vendedor'] == vendedor]['vendas'].values


# print(round(df['vendas'],2))
# print(round(df['vendedor']))
def linha():
    plt.plot(df['vendedor'],dados['vendas'])
    plt.xlabel("Vendedor")
    plt.ylabel("Vendas")
    plt.title('GRAFICO DE LINHA ')

    plt.show()

def pizza():
    plt.pie(df['vendas'], labels= df['vendedor'],autopct='%1.1f%%')
    plt.title('GRAFICO DE PIZZA')
    plt.ylabel("Vendedor")
    plt.xlabel("Vendas")
    plt.title('GRAFICO DE PIZZA')

    plt.show()



def dispersao():
    plt.scatter(df['vendas'], df['vendedor'])
    plt.title('GRAFICO DE DISPERSÃO')

    plt.show()

def barra():
    plt.bar(df['vendedor'], df['vendas'])
    plt.xlabel("vendedor")
    plt.ylabel("vendas") 
    plt.title('GRAFICO DE BARRAS')
    
    plt.show()

def boxplot_vendas_por_vendedor():
    df.boxplot(column='vendas', by='vendedor')
    plt.title('BOX PLOT DE VENDAS POR VENDEDOR')
    plt.ylabel('Vendas')
    plt.xlabel('Vendedor')
    plt.show()

def grafico_violino_vendas_por_vendedor():
    plt.figure()
    sns.violinplot(x='vendedor', y='vendas', data=df)
    plt.title('GRÁFICO DE VIOLINO DE VENDAS POR VENDEDOR')
    plt.ylabel('Vendas')
    plt.xlabel('Vendedor')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


janela = tk.Tk('')
janela.title('Graficos de Vendas')


janela.geometry('300x310')


texto =  tk.Label(janela, text='Qual grafico você quer gerar, escolha 1')
texto.pack()

btn_ = tk.Button(janela, text='Grafico de Linha',command=linha, bg='lightblue')
btn_.pack()

btn_ = tk.Button(janela, text='Grafico de Pizza',command=pizza, bg='lightblue')
btn_.pack()

btn_ = tk.Button(janela, text='Grafico de Dispersao',command=dispersao, bg='lightblue')
btn_.pack()

btn_ = tk.Button(janela, text='Grafico de Barra',command=barra, bg='lightblue')
btn_.pack()

btn_boxplot = tk.Button(janela, text='Box Plot de Vendas', command=boxplot_vendas_por_vendedor, bg='lightblue')
btn_boxplot.pack()

texto_titulo = tk.Label(janela, text='Análise Estatística de Vendas', font=('Arial', 14, 'bold'))
texto_titulo.pack(pady=10)

maior_venda = df['vendas'].max()
menor_venda = df['vendas'].min()
media_vendas = df['vendas'].mean()
mediana_vendas = df['vendas'].median()
desvio_padrao_vendas = df['vendas'].std()

texto_maior = tk.Label(janela, text=f'Maior Venda: {maior_venda:.2f}')
texto_maior.pack()

texto_menor = tk.Label(janela, text=f'Menor Venda: {menor_venda:.2f}')
texto_menor.pack()

texto_media = tk.Label(janela, text=f'Média das Vendas: {media_vendas:.2f}')
texto_media.pack()

texto_mediana = tk.Label(janela, text=f'Mediana das Vendas: {mediana_vendas:.2f}')
texto_mediana.pack()

texto_desvio = tk.Label(janela, text=f'Desvio Padrão das Vendas: {desvio_padrao_vendas:.2f}')
texto_desvio.pack()

janela.mainloop()