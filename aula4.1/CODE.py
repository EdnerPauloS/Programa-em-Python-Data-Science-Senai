# Crie um sistema de banco, com as seguintes operações:
# COM LOOPS - CONDICIONAIS  -  VARIÁVEIS -  LISTAS - DICIONÁRIOS. 
# SISTEMA DE BANCO 


SENHA = '123456'
LOGIN =  '@KARLA'
saldo = [5000]

c = 3
for n in range(1,c+1):

            for  i in range(1,4):
                login = input('Digite seu login: ')
                senha = input('Digite a senha: ')
                if LOGIN == login and senha == SENHA:
                    print('ESCOLHA A OPERAÇÃO:')
                    escolha =  input('escolha a operação 1 saque | 2 deposito | saldo:')
                    if escolha == '1':
                        saque = float(input('Digite o valor do saque: ')) 
                        saldo1 = sum(saldo)
                        v = saldo1 - saque
                        print(v)
                        break
                    elif escolha  == '2': 
                        deposito = float(input('Digite o valor do deposito: ')) 
                        v = v + deposito
                        print(v)
                      
                        break
                    
                    elif escolha  == '3':
                          print('Saldo', v)
                          break
                    else:
                         print('Digite alvo valído')   
                else:
                     print('Acesso negado')
            else:
               print('Conta bloqueada')    
               c = c +1 

SAIR  =  input('Digite enter para sair')
   





# - Sair do sistema 
# # (DESPEDIR)


# enquanto 
# for finito X infinito


acesso = input('Deseja acessar?')
carrinho =  []
while acesso == 'sim':
    print('Olá ')
    lista = [1,2,3,4,5,6]
    
    print('escolha um valor')
    v =  int(input('>>'))
    carrinho.append(lista[v])
    print(carrinho)
    acesso = input('Deseja continuar?')
else:
    print('Obrigada volte sempre') 