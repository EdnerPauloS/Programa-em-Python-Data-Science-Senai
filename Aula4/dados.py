# loja virtual com loop for:

# CADASTRANDO O USUÁRIO NA LOJA VIRTUAL
dados = {'login': [], 'senha':[]}

for n in range(1,2):
    login = input('Digite o login')
    senha = input('Digite a senha ')
    dados['login'].append(login)
    dados['senha'].append(senha)
print(dados)    



l = [1,2,3]
for i in l:# faz o loop para acertar a login
        login_usuario = input('Digite o login: ')# 
        senha    = input('Digite a senha: ')
        if login_usuario in dados['login'] and senha in dados['senha']:
                print('Seja bem vindo!')
                lista_prod = ['','CELULAR MOTOG', 'IPHONE 16', 'PC GAME DELL']
                valores = ['',1500.0,6000.0,5000.0]
                print(lista_prod)
                print('R$ ', valores)
                quantidade_prod = int(input('Quantos produtos?'))
                carrinho = []
                valores_user = []
                for n in range(1,quantidade_prod+1):
                    produto_user = int(input('Escolha o produto pelo ID - 1 - 2 -3'))
                    carrinho.append(lista_prod[produto_user])
                    print(carrinho)
                    valores_user.append(valores[produto_user])
                    print('R$', valores_user)
                    s = sum(valores_user)
                    print('Sua compra - R$', s)
                    
                else:
                    print('Obrigada volte sempre!')   
                    break
        else:
           print('Acesso negado')
else:
     print('conta bloqueada')  