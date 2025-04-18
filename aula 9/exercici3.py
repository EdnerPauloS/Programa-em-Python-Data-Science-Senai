import matplotlib.pyplot as plt

# Dados
medias_jose = [10, 5, 8, 9, 10, 5, 4]
meses = ['fev', 'mar', 'abril', 'maio', 'junho', 'julho', 'agosto']

# # Criando o gráfico de barras
# plt.bar(meses, medias_jose, color='orange')

# # Adicionando título e rótulos aos eixos
# plt.title("Médias de José ao Longo dos Meses")
# plt.xlabel("Meses")
# plt.ylabel("Média")

y_pos = range(len(meses))
# Criando o gráfico de barras horizontais
fig, ax = plt.subplots()
ax.barh(y_pos, medias_jose, align='center', color='gold')

# Definindo os rótulos do eixo y
ax.set_yticks(y_pos)
ax.set_yticklabels(meses)

# Invertendo o eixo y para que o primeiro mês fique no topo
ax.invert_yaxis() 

# Adicionando título e rótulos aos eixos
ax.set_xlabel("Média")
ax.set_title("Médias de José ao Longo dos Meses")








# Exibindo o gráfico
plt.tight_layout()  # Ajusta o layout para que os rótulos não se sobreponham
plt.show()
