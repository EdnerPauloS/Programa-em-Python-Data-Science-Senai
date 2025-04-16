import numpy as np 

# Crie um array 2D de tamanho (5, 5) com valores aleatórios entre 0 e 100.
ar_ = np.random.randint(0, 101,(5, 5))  # Gera um array 5x5 com valores aleatórios entre 0 e 100
print("Array 5x5 com valores aleatórios:")
print(ar_)
print()

r = ar_ [ar_ % 2 == 0 ]  
print(r)
ra = np.sort(r)
print(ra)
print()

re = ar_ [ar_ % 2 == 1 ]  
print(re)
ren = np.sort(re)
print(ren)

# Calcule a média de cada linha.
media_por_linha = np.mean(ar_)  
print(f"\nMédia de cada linha: {media_por_linha}")

# Encontre o valor máximo e mínimo de toda a matriz.
valor_maximo = np.max(ar_)  # Encontra o valor máximo
valor_minimo = np.min(ar_)  # Encontra o valor mínimo
print(f"\nValor máximo da matriz: {valor_maximo}")
print(f"Valor mínimo da matriz: {valor_minimo}")



vendas = np.array([120,90,150,80,200,110,50,300])
# Filtre apenas as vendas maiores que 100.

filtro = vendas > 100
x = vendas[filtro]
print(f"\nValor maiores que 100 são: {x}")

# Calcule quantas vendas ficaram abaixo da média.
media = np.mean(vendas)
print(f"\nValor da media é: {media}")

abaixo = len(vendas[vendas < np.mean(vendas)])
print(f"\nValor abaixo da media : {abaixo}")
# Crie um novo array com os valores normalizados (divida cada valor pelo máximo).

# nova array 
nova  =  [vendas/np.max(vendas)]
print(f"\nValor do novo array: {nova}")