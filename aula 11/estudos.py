import matplotlib.pyplot as plt
import pandas as pd
# lendo um csv
dados = pd.read_csv('student_habits_performance.csv')

# print(dados)
# print(dados.info())
# print(dados.describe())

#tranformando em um data freme
df = pd.DataFrame(dados)
# print(df)

#renomear nomes em ingles
dados = dados.rename(columns={
    
})