# variavel = 50

# lista = [1,2,3,4,5,6]
# print(lista[0],lista[3])
# print(lista[-2])

# # # texto str() 'text'
# # # inteiro int()  12
# # # reais float()  0.5
# # # logicos bool()  True
# # # ---------------
# # # variáveis  -  espaços na memória do pc
# # # nome  = valor do tipo primitivo 
# # # ------------------------------
# # # input()
# # # print()
# # # -------------------------------


# # variavel = 50
# # # direita para esquerda -1 
# # lista = [1,2,3,4,5,6]
# # lista_float = [1.2,5.2,3.8]
# # lista_string = ['txt',' texto', 'a']
# # lista_boleana  = [True, False]
# # lista_mista = [True, 'Texto', 200, 5.0]


# # # Acessando um dado de uma lista


# # lista = [1,2,3,4,5,6]
# # soma = lista[0] * lista[5]
# # print(soma)
# # # print(lista)
# # # print(lista[3])
# # # # mudar o valor manualmente


# # # lista[2] = "Ana"
# # # print(lista)
# # nomes = [input(), input(), input(), input()]
# # print(nomes)


# # #input()


# # nome  =  input('Digite seu nome: ')
# # print(nome) 
# # # funções para manipular listas alteram o formato da lista:


# lista = [1,5,3,6,6,660]
# # adicionar um dado *********


# lista.append(250)
# lista.append(300)
# lista.append(250)


# lista += (300,200,500,2500,100,100,250,250,250)
# lista.extend([250,250,250])


print('Mercado xx')
lista_aninhada = [['fone','tv','celular'],[150.0,5000.0,600.0]]

sessao = int(input('Escolha sua sessão'))
print(lista_aninhada[sessao])

produto_1 = int(input('Digite o produto pelo ID'))
print(lista_aninhada[sessao][produto_1])

produto_2 = int(input('Digite o produto pelo ID'))
print(lista_aninhada[sessao][produto_2])

produto_3 = int(input('Digite o produto pelo ID'))
print(lista_aninhada[sessao][produto_3])

meus_produtos =  [lista_aninhada[sessao][produto_1], lista_aninhada[sessao][produto_2], lista_aninhada[sessao][produto_3]]
print('Meus produtos', meus_produtos)
valor_prod = [lista_aninhada[1][produto_1],lista_aninhada[1][produto_2],lista_aninhada[1][produto_3] ]
print('R$', valor_prod)

print('****' * 20)

somar = sum(valor_prod)
print('Total da compra - R$', somar)

# lista_nomes = ['Ana', 'Fernanda', 'Caio']
# debitos = [5000.0,25000.0,2500.0]
# idade = [35,51,25]


# # média
# # maior debitos
# # menor debito


# media =  sum(debitos)/len(debitos)
# media_idade = sum(idade)/len(idade)
# menor_d = min(debitos)
# maior_d = max(debitos)


# print('Maior', maior_d)
# print('Menor' , menor_d)
# print('media debitos: ', round(media))
# print('media idade: ', round(media_idade))
