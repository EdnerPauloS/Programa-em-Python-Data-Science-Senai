import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dados = pd.read_csv('desafiodados.csv')


df = pd.DataFrame(dados)
df.sort_index()

print(round(df['vendas'],2))
# print(round(df['vendedor']))

plt.figure(figsize=(8,9))
plt.plot(df['vendedor'],dados['vendas'])
valores_y = [0, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000 ]  
plt.yticks(valores_y) 
plt.ylim(0, 50000)
plt.xlabel("Vendedor")
plt.ylabel("Vendas")

plt.show()
