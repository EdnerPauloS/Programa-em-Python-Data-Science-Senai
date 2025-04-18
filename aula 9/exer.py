import matplotlib.pyplot as plt
import statistics


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
empresa1 = [1000,6000,1200,8000,1400]
empresa2 = [5000,4000,3000,2000,7000]
empresa3 = [1200,1300,8000,3000,15000]
empresa4 = [1400,1750,2000,4500,5900]

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

# Gerando gráfico
fig, ax = plt.subplots(figsize=(10, 6))

# Plotando as métricas de cada empresa
for i, metrica in enumerate(metricas):
    ax.bar(empresas, [valores[j][i] for j in range(len(valores))], label=metrica, alpha=0.7)

# Configurações do gráfico
ax.set_ylabel('Valores')
ax.set_title('Estatísticas das Empresas')
ax.legend(title='Métricas')

plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

input('Pressione Enter para sair')
