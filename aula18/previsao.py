import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import ttk

from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

df = pd.read_csv('titanic.csv')


df['Age'].fillna(df['Age']).median()
df['Sex'] = LabelEncoder().fit_transform(df['Sec'])
df['Pclass'] = df['Pclass'].astype('category')

root = tk.Tk()
root.geometry('1200x900')

frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=10, fill=tk.BOTH, expand= True )


frame_controle = tk.Frame(root)
frame_controle = tk.Frame(root)

frame_resultado = tk.Frame(root)
frame_resultado.pack(pady=10)

label_tendencia = tk.Label(frame_resultado,text='',justify=tk.LEFT)
label_tendencia.pack()

label_descricao = tk.Label(frame_resultado,text='',justify=tk.LEFT)
label_descricao.pack()

label_previsao = tk.Label(frame_resultado,text='',justify=tk.LEFT)
label_previsao.pack()

def limpar_frame():
    for w in frame_grafico.winfo_children():
        w.destroy

def mostrar_barras():
    limpar_frame()
    fig,ax = plt.subplots(figsize=(8,5))
    sobreviventes_por_classe = df.groupby('Pclass')['Suviver'].mean()
    sobreviventes_por_classe.plot(kind='bar',color=['red','blue','yelow'])


    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill=tk.BOTH, expand=True)

    insight = 'Passageriros da 1ª classe tiveram a maior taxa de sobrevivencia'
    label_tendencia.config(insight)

def mostrar_linhas():
    limpar_frame()
    fig,ax = plt.subplots(figsize=(8,5))

    idade_medias_sobreviventes = df[df['Surviver']==1].groupby('Pclass')['Age'].mean
    idade_medias_nao_sobreviventes = df[df['Surviver']==0].groupby('Pclass')['Age'].mean

    idade_medias_sobreviventes.plot(kind='line', label = 'Sobreviventes', ax = ax)
    idade_medias_nao_sobreviventes.plot(kind='line', label = 'Sobreviventes', ax = ax)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill=tk.BOTH, expand=True)

    insight = 'Passageriros da 3ª classe tiveram a menor taxa de sobrevivencia'
    label_tendencia.config(insight)

def mostrar_tendencia():
    limpar_frame()
    idade_media = df['Age'].mean()
    idade_mediana = df['Age'].median()
    idade_moda = df['Age'].mode()

    tarifa_media = df['Fare'].mean()
    tarifa_mediana = df['Fare'].median()
    tarifa_moda = df['Fare'].mode()[0]

    resultado = (
        f'Idade média {idade_media} anos \n'
        f'Idade mediana {idade_mediana} anos \n'
        f'Idade moda {idade_moda} anos \n'
        f'Tarifa média {idade_media} anos \n'
        f'Tarifa mediana {idade_mediana} anos \n'
        f'Tarifa média {idade_moda} anos \n'
    )

    label_tendencia.config(resultado)
    insight = 'A mediana da Tarifa é menor que a media, que indica que poucos passageriros pagaram valores elevados'
    label_tendencia.config(insight)

def mostrar_describe():
    limpar_frame()
    descricao = df['Age', 'Fare', 'Pclass', 'Surviver' ].describe().to_string()
    label_descricao.config(text=descricao)
    
    insight = '75 "%" dos Passageiros pagaram r$ 31 libras o máximo 512.00(grande diferença)'
    label_descricao.config(insight)
    

def mostrar_previsao():
    limpar_frame()

    features = ['Pclass', 'Sex', 'Age', 'Fare']
    X = df[features]
    y = df['Surviver']

    X_train, X_test, y_train, y_test = train_test_split(X,y , test_size=0.2, random_state=42)

    model = RandomForestClassifier(n_estimators=100, random_state= 42)
    model.fit(X_train, y_train)
 
    y_pred = model.predict(X_test)

    importancia= pd.Series(model.feature_importances_,index=features).sort_values(ascending=False)

    fig,ax = plt.subplot(figsize=(8,5))
    importancia.plot(kind='bar', ax= ax)

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.draw()
    canvas.get_tk_widget().pack(side='top', fill=tk.BOTH, expand=True)

    label_descricao.config(text=y_pred)
    insight = 'O fator principal para sobreviver no titaniv e através do Sexo - Feminino'
    label_descricao.config(insight)


btn_barras = ttk.Button(frame_controle, text='Grafico de Barras', command= mostrar_barras)
btn_barras.grid(row=0, column=0,padx= 5, pady=5)

btn_linhas = ttk.Button(frame_controle, text='Grafico de Linhas', command= mostrar_linhas)
btn_linhas.grid(row=1, column=0,padx= 5, pady=5)

btn_tendencia = ttk.Button(frame_controle, text='Tendencia', command= mostrar_tendencia)
btn_tendencia.grid(row=2, column=0,padx= 5, pady=5)

btn_describe = ttk.Button(frame_controle, text='Descrição', command= mostrar_describe)
btn_describe.grid(row=2, column=0,padx= 5, pady=5)

btn_previsao = ttk.Button(frame_controle, text='Previsão', command= mostrar_previsao)
btn_previsao.grid(row=2, column=0,padx= 5, pady=5)




root.mainloop()