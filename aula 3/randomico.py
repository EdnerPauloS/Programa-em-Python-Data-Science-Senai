import random


dicionario ={'calça': 50.00 , 'camiseta': 45.00, 'meias': 20.00 }
print(dicionario)
pedido  =  input('Escolha um produto; ')
valor  =  random.randrange(10,150)
dicionario[pedido] = float(valor)
print('Seu carrinho: ', dicionario)

soma = 0
for chave, valor in dicionario.items():
    print(chave, ':', valor )
    soma = soma + valor

print('Total, R$: ', soma) 


# import random





# numero = random.randint(1,10)


# print(numero)



# mercado = {
   
# 'arroz':15.00,
# 'feijão':5.00,
# 'carne 1kg': 20,
# 'refrigerante': 14.00


# }
# # pedido1 = input('Digite o produto:')
# # pedido2 = input('Digite o produto:')
# # pedido3 = input('Digite o produto:')


# # tupla_valores = mercado[pedido1], mercado[pedido2], mercado[pedido3]


# # lista = list(tupla_valores)


# # print(tupla_valores)


# # soma  =  sum(lista)


# # print('R$', soma)



# print(mercado.items())


# print(mercado.get('arroz'))