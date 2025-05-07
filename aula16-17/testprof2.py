import sqlite3
import matplotlib.pyplot as plt
import pandas as pd

# criando o banco 
conexao = sqlite3.connect('meu_banco2.bd')

# posso introduzir o sql no código 
cursor =  conexao.cursor()

# criar tabela 
cursor.execute('''
      CREATE TABLE IF NOT EXISTS clientes(
             id INTEGER PRIMARY KEY AUTOINCREMENT,
             nome TEXT NOT NULL,
             idade INTEGER NOT NULL,
             email TEXT NOT NULL,
             cidade TEXT NOT NULL        
    )
''')

# INSERIR OS DADOS

cursor.execute("INSERT INTO clientes(nome, idade, email,cidade) VALUES ('Maria', 30, 'maria@gmail.com','SÃO PAULO')")
cursor.execute("INSERT INTO clientes(nome, idade, email,cidade ) VALUES ('Lucas', 25, 'lucas@gmail.com', 'SÃO PAULO')")
cursor.execute("INSERT INTO clientes(nome, idade, email,cidade ) VALUES ('Carlos', 35, 'carlos@gmail.com','GUARULHOS ')")
cursor.execute("INSERT INTO clientes(nome, idade, email,cidade ) VALUES ('CarlA', 35, 'carla@gmail.com','BELO HORIZONTE')")

conexao.commit()


cursor.execute("SELECT * FROM clientes")

LISTA_ID  =  []
LISTA_NOMES  =  []
LISTA_IDADE = []
LISTA_CIDADE  =  []
LISTA_EMAILS = []


for dados in cursor.fetchall():
    LISTA_ID.append(dados[0])
    LISTA_NOMES.append(dados[1])
    LISTA_IDADE.append(dados[2])
    LISTA_CIDADE.append(dados[4])
    LISTA_EMAILS.append(dados[3])
# print(LISTA)

data =  {
    'id': LISTA_ID,    
    'nomes':LISTA_NOMES,
    'idades':LISTA_IDADE,
    'cidades':LISTA_CIDADE,
    'emails':LISTA_EMAILS
}

df = pd.DataFrame(data)

df.to_csv('dados_do_banco1.csv')
# print(data)
media  = df.groupby('cidades')['idades'].mean()
print(media)


cursor.close()
plt.figure(figsize=(10,6))
# plt.pie( LISTA_IDADE,labels= LISTA_CIDADE,  autopct='%1.1f%%', colors = ['red', 'green','blue', 'yellow'])
plt.pie( media,labels= ['SÃO PAULO','GUARULHOS','BELO HORIZONTE'],  autopct='%1.1f%%', colors = ['red', 'green','blue', 'yellow'])
plt.show()

