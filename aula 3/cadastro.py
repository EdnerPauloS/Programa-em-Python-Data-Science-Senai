

dados_usuarios ={}
print('Seja bem vindo, cadastre-se: ')

nome  = input('Nome: ')
login = input('Login: ')
senha = input('Senha : ')

dados_usuarios['nome']  = nome
dados_usuarios['login'] = login
dados_usuarios['senha'] = senha

print(dados_usuarios)
login_usuario = input('Login: ')
senha_usuario = input('Senha: ')
carrinho = []
if senha_usuario in dados_usuarios['senha']  and login_usuario in dados_usuarios['login']:
   print('Seja bem vindo:  ', dados_usuarios['nome'])
   lista_prod = ['a','b', 'c']
   escolha =  int(input('Escolha o produto a partir do ID 0,1,2'))
   carrinho.append(lista_prod[escolha])
   print(carrinho)