import pandas as pd


dici = {

    'vendas':[1000,200,300,400,500,600],
    'vendedor':['a','b','c','d','e','f']
}

df= pd.DataFrame(dici)
df.to_csv('dados.csv')

dados = pd.read_csv('dados.csv')
coluna = dados['vendas']
print(coluna)