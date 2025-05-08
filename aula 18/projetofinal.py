import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import tkinter as tk
from tkinter import messagebox
import sqlite3
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

# Criando um dataset fictício
data = {
    'Aluno': ['Aluno1', 'Aluno2', 'Aluno3', 'Aluno4', 'Aluno5'],
    'Nota_1': [7.5, 8.0, 6.0, 9.0, 7.8],
    'Nota_2': [8.0, 7.5, 5.5, 9.2, 8.1],
    'Nota_Final': [8.0, 7.7, 5.8, 9.1, 8.0], 
    'Presenca': [90, 85, 78, 95, 88],  
    'Atividades_Extra': [3, 2, 1, 5, 4]  
}

df = pd.DataFrame(data)

# Função para exibir o dataset em uma nova janela
def show_data():
    new_window = tk.Toplevel(window)
    new_window.title("Dados dos Alunos")
    text = tk.Text(new_window)
    text.insert(tk.END, df.to_string())
    text.pack()

# Configuração da interface
window = tk.Tk()
window.title("Análise de Desempenho Acadêmico")

btn_show_data = tk.Button(window, text="Exibir Dados", command=show_data)
btn_show_data.pack()

# Gerando os gráficos ANTES de rodar o Tkinter
def plot_graphs():
    # Remover a coluna 'Aluno' da análise de correlação, pois ela não é numérica
    df_numeric = df.drop(columns=['Aluno'])

    # Plotando a correlação entre as variáveis
    plt.figure(figsize=(8, 6))
    sns.heatmap(df_numeric.corr(), annot=True, cmap='coolwarm')
    plt.title("Correlação entre Variáveis")
    plt.show()

    # Scatterplot para visualizar a relação entre presença e nota final
    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='Presenca', y='Nota_Final', data=df)
    plt.title("Relação entre Presença e Nota Final")
    plt.xlabel("Presença (%)")
    plt.ylabel("Nota Final")
    plt.show()

# Gerando os gráficos
plot_graphs()

# Iniciando a interface gráfica
window.mainloop()

# Definindo as variáveis independentes e dependentes de forma segura
X = df.select_dtypes(include=[float, int]).drop('Nota_Final', axis=1)
y = df['Nota_Final']

# Dividindo os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Criando e treinando o modelo
model = LinearRegression()
model.fit(X_train, y_train)

# Fazendo previsões
y_pred = model.predict(X_test)

# Exibindo o erro médio quadrático
mse = mean_squared_error(y_test, y_pred)
print(f"Erro Médio Quadrático (MSE): {mse}")
