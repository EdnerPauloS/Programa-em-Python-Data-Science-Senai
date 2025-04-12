import math
x=()
dados = [1, 2, 3, 4, 5]
media = sum(dados) / len(dados)
variancia = sum((x - media)  2 for x in dados) / len(dados)



desvio_padrao = math.sqrt(variancia)
print(f"Desvio Padrão: {desvio_padrao}")
