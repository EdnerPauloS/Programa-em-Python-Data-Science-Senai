import num as np
# Crie um array 2D de tamanho (5, 5) com valores aleatórios entre 0 e 100.

# Calcule a média de cada linha.

# Encontre o valor máximo e mínimo de toda a matriz.



# Cria um array 2D de 0 a 99 e o reorganiza em uma matriz 5x5
ar = np.arange(100).reshape((5, 20))  # Corrigido para 5x20
print("Array original (5x20):")
print(ar)

# Se você quiser um array 5x5, você deve usar:
ar_5x5 = np.arange(25).reshape((5, 5))  # Cria um array 5x5 com valores de 0 a 24
print("\nArray 5x5:")
print(ar_5x5)

# Exemplo de operações com o array 5x5
# 1. Acessar um elemento específico
elemento = ar_5x5[2, 3]  # Acessa o elemento na 3ª linha e 4ª coluna
print(f"\nElemento na 3ª linha e 4ª coluna: {elemento}")

# 2. Calcular a soma de todos os elementos
soma_total = np.sum(ar_5x5)
print(f"Soma de todos os elementos: {soma_total}")

# 3. Calcular a média dos elementos
media = np.mean(ar_5x5)
print(f"Média dos elementos: {media}")

# 4. Transpor o array
transposto = ar_5x5.T
print("\nArray transposto:")
print(transposto)

# 5. Adicionar 10 a todos os elementos
adicionado = ar_5x5 + 10
print("\nArray após adicionar 10 a todos os elementos:")
print(adicionado)