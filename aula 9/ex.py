import matplotlib.pyplot as plt
import statistics
import numpy as np

def moda1(lista):
    return statistics.mode(lista)

def mediana1(lista):
    return statistics.median(lista)

def varianca1(lista):
    return statistics.variance(lista)

def desvio1(lista):
    return statistics.stdev(lista)

def media1(lista):
    return statistics.mean(lista)

# Dados das empresas
empresa1 = [1000, 6000, 1200, 8000, 1400]
empresa2 = [5000, 4000, 3000, 2000, 7000]
empresa3 = [1200, 1300, 8000, 3000, 15000]
empresa4 = [1400, 1750, 2000, 4500, 5900]

# Função que retorna as métricas para cada empresa
def handle(lista):
    media = media1(lista)
    mediana = mediana1(lista)
    moda = moda1(lista)
    varianca = varianca1(lista)
    desvio = desvio1(lista)
    return media, mediana, moda, varianca, desvio

# Coletando as estatísticas de todas as empresas
resultado = {
    "Empresa 1": handle(empresa1),
    "Empresa 2": handle(empresa2),
    "Empresa 3": handle(empresa3),
    "Empresa 4": handle(empresa4)
}

# Organizando os resultados para o gráfico
metricas = ['Média', 'Mediana', 'Moda', 'Variância', 'Desvio Padrão']
empresas = list(resultado.keys())
valores = list(resultado.values())

# Número de empresas
n_empresas = len(empresas)

# Largura das barras
bar_width = 0.15

# Posições das barras no eixo X para as empresas
indices = np.arange(n_empresas)

# Cores diferentes para cada métrica
cores = ['#FF5733', '#33FF57', '#3357FF', '#F3FF33', '#FF33A8']

# Gerando gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Plotando as métricas de cada empresa com barras separadas e cores diferentes
for i, metrica in enumerate(metricas):
    # Para cada métrica, plotamos uma barra para cada empresa
    ax.bar(indices + i * bar_width, [valores[j][i] for j in range(len(valores))], 
           width=bar_width, label=metrica, alpha=0.7, color=cores[i])

# Configurações do gráfico
ax.set_ylabel('Valores')
ax.set_title('Estatísticas das Empresas')
ax.set_xticks(indices + bar_width * (len(metricas) - 1) / 2)  # Ajustando as posições das empresas
ax.set_xticklabels(empresas)

# Adicionando a legenda
ax.legend(title='Métricas')

# Melhorando o layout
plt.xticks(rotation=45)
plt.tight_layout()

# Exibindo o gráfico
plt.show()

input('Pressione Enter para sair')
