import sqlite3
import matplotlib.pyplot as plt

# criando o banco 
conexao = sqlite3.connect('meu_banco.bd')

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

LISTA  =  []
LISTA_IDADE = []
for dados in cursor.fetchall():
    LISTA.append(dados[2])
    LISTA_IDADE.append(dados[4])
print(LISTA)


cursor.close()
plt.figure(figsize=(10,6))
plt.bar( LISTA_IDADE, LISTA,   color ='red')
plt.show()
