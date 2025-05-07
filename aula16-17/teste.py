import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

conexao = sqlite3.connect('meu_banco1.bd')
cursor = conexao.cursor()

cursor.execute('''
        CREATE TABLE IF NOT EXISTS clientes(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INTEGER NOT NULL,
                email TEXT NOT NULL,    
                cidade TEXT NOT NULL    
    )
               
''')

cursor.execute("INSERT INTO clientes(nome,idade,email,cidade) VALUES('Maria',30, 'maria@gmail.com','Guarulhos')")
cursor.execute("INSERT INTO clientes(nome,idade,email, cidade) VALUES('Mariana',15, 'mariana@gmail.com','São Paulo')")
cursor.execute("INSERT INTO clientes(nome,idade,email,cidade) VALUES('Lucas',24,'lucas@gmail.com','Guarulhos')")
cursor.execute("INSERT INTO clientes(nome,idade,email,cidade) VALUES('Demetrius',24,'demetrius@gmail.com','Jaçana')")

conexao.commit()


cursor.execute("SELECT*FROM clientes")

lista=[]
lista_idades=[]
lista_cidades=[]

data ={
    'idades':lista_idades,
    'cidades':lista_cidades,
}

df = pd.DataFrame(data)

df.to_csv('dados_do_bandco.csv')

print(data)


for dados in cursor.fetchall():
    lista.append(dados[2])
    lista_idades.append(dados[4])
print(lista)

cursor.close()
plt.figure(figsize=(10,6))
plt.bar( lista_idades, lista,   color ='red')
plt.show()
