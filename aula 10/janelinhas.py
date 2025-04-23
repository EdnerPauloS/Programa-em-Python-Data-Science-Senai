import tkinter as tk



janela = tk.Tk()


janela.geometry('250x250')


texto =  tk.Label(janela, text='isso é um texto',bg='red')
texto.pack()


entry_text = tk.Entry(janela)
entry_text.pack()


btn_ = tk.Button(janela, text='clique aqui')
btn_.pack()



janela.mainloop()



# wigets = botão, input, texto sobre ainterface
# frames (espaços para guardar informações)
# tree  