
import pandas as pd


# 2. Criando DataFrames
# - De um dicionário:

data = {'coluna1': [1, 2, 3], 'coluna2': [4, 5, 6]}
df = pd.DataFrame(data)

data2 = {'a':[1,2,3],'b':[1,2,3]}
df2 = pd.DataFrame(data2)
# - De uma lista de listas:

data = [[1, 4], [2, 5], [3, 6]]
df = pd.DataFrame(data, columns=['coluna1', 'coluna2'])

print(data)
