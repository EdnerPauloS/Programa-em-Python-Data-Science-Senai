import matplotlib.pyplot as plt

# Dados
ano = [2021, 2022, 2023, 2024, 2025, 2026]
vendas = [10000, 2000, 30000, 10000, 5000, 20000]

# Criando o gráfico de linha (plot)
plt.plot(ano, vendas)

# Adicionando título e rótulos aos eixos
plt.title("Vendas ao Longo dos Anos")
plt.xlabel("Ano")
plt.ylabel("Vendas (em unidades)")

# Exibindo o gráfico
plt.grid(False)

plt.show()
