
meu_dicionario = {}
dic = dict()    # cria um dicionario vazil
print(meu_dicionario)

meu_dicionario = {'a': 1, 'b': 2, 'c': 3}
print(meu_dicionario['a'])  # me mostra o escolhido  valor

meu_dicionario['d'] = 4 # desta forma acrescenta um novo item
print(meu_dicionario) 

# del meu_dicionario['a']
# print(meu_dicionario)

print(meu_dicionario.keys()) #tras as keys ou chaves

print(meu_dicionario.values()) #traz os valores

print(meu_dicionario.items()) #traz tudo os valores e keys

print(meu_dicionario.get('b'))# mostra o valor selecionado

valor = meu_dicionario.pop('c')# exclue a selecionada
print(valor)  # Saída: 3
print(meu_dicionario)

meu_dicionario.clear()# limpa
print(meu_dicionario)

