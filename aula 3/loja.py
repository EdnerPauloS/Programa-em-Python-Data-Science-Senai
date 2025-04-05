# variáveis  -  listas - tuplas -  
# conjuntos - dicionais 

print('Cadastre-se:')

dados = {'login':input('cadastre seu login:'),
         'senha':input('cadatre uma senha: ')}


loja = {
'tv': 5000,
'microondas':200,
'celular':1500
}

dados['email'] = input('cadatre uma email: ')

print('Acesse com senha e login')

login = input('digite seu login: ')
senha = input('Digite sua senha: ')


if login == dados['login'] and senha == dados['senha']:
    print('Seja bem vindo(a)')
    print('Produtos disponíveis:', list(loja.keys()))
    produto1 = input('Digite o nome do produto ')
    produto2 = input('Digite o nome do produto ')
    lista_prod = [produto1,produto2] 
    lista_valores = [loja[produto1],loja[produto2]]
    soma  = sum(lista_valores)
    print('seus produtos:', lista_prod)
    print('R$',soma)
    # Novo pedido
    novo_pedido = input('Deseja fazer um novo pedido? (s/n): ')
    if novo_pedido == 's':
        while True:
            produto3 = input('Digite o nome do produto: ')
            if produto3 in loja:
                lista_prod.append(produto3)
                lista_valores = [loja[produto] for produto in lista_prod]
                soma = sum(lista_valores)
                break
            print('Produto inválido. Tente novamente.')

        print('Seus produtos:', lista_prod)
        print('Total: R$', soma)
        print('Obrigado e volte sempre')

    # Retirar produto
    excluir_pedido = input('Deseja retirar algum pedido? (s/n): ')
    if excluir_pedido == 's':
        while True:
            produto4 = input('Digite o nome do produto a ser retirado: ')
            if produto4 in lista_prod:
                lista_prod.remove(produto4)
                lista_valores = [loja[produto] for produto in lista_prod]
                soma = sum(lista_valores)
                print('Seus produtos:', lista_prod)
                print('Total: R$', soma)
                print('Seus produtos:', lista_prod,' foi retirado com sucesso')
                print('Obrigado e volte sempre')
                
                break
            print('Produto não encontrado. Tente novamente.')
else:
    print('Acesso negado')    