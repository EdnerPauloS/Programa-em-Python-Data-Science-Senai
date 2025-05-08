from sklearn.linear_model import LinearRegression
import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


def carregar():
    caminho = filedialog.askopenfilename(filetypes=[('CSV files', '*csv')])
    if caminho:
        global df
        df = pd.read_csv(caminho)
        label_status.config(text= 'Carregar csv')

def previsao_1():
    X = np.array(df.index).reshape(-1,1)
    y = df['Tempo_espera']
    
    modelo = LinearRegression()
    modelo.fit(X,y)

    previsao = modelo.predict([[len(df)+1]])
    label_previsao.config(text=f'{previsao[0]:.2f}minutos')



# def carregar_dispersao():
#     fig,ax = plt.subplots(figzise=(6,4))
#     ax.scatter(df['Tempo_espera'], df.index, color='red')

#     canvas = FigureCanvasTkAgg(fig, master=frame_grafico )
#     canvas.get_tk_widget().pack(side=tk.RIGHT,padx=10)
#     canvas.draw()

#     print(df.index)



def carregar_dispersao():
    fig,ax = plt.subplots(figsize=(6,4))
    ax.scatter(df['Tempo_espera'], df.index, color='red')

    canvas = FigureCanvasTkAgg(fig, master=frame_grafico)
    canvas.get_tk_widget().pack(side=tk.RIGHT,padx=10)
    canvas.draw()
    
    print(df.index)


# def carregar_linhas():
#     df = df['']


#janela

root = tk.Tk()
root.title('DASHBOARD')
root.geometry('1200x900')

frame_grafico = tk.Frame(root)
frame_grafico.pack(pady=20,side=tk.TOP,fill=tk.X)

btn_linhas = tk.Button(root, text='Linhas')
btn_linhas.pack(pady=5, side=tk.TOP)

btn_dispensao = tk.Button(root, text='Dispensão',command= carregar_dispersao)
btn_dispensao.pack(pady=5, side=tk.TOP)

btn_previsao = tk.Button(root, text='Previsão de tempo de atendimento', command=previsao_1)
btn_previsao.pack(pady=5, side=tk.TOP)

label_previsao = tk.Label(root)
label_previsao.pack(pady=5, side=tk.TOP)

btn_carregar = tk.Button(root, text='Carregar dados' , command=carregar)
btn_carregar.pack(pady=5, side=tk.TOP)

label_status = tk.Label(root, text='Carregue os Dados')
label_status.pack(pady=10, side=tk.TOP)

root.mainloop()
