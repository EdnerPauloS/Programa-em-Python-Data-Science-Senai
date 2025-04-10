import time
# SISTEMA DE BANCO 
conta = [1, 2, 3, 4]
login = ['Paulo', 'Daniel', 'Felipe', 'Gustavo']
login = [nome.lower() for nome in login]  # Corrigido: tudo minúsculo
saldo = [3000, 1500, 4000, 1000]
deposito = [0, 0, 0, 0]
saque = [0, 0, 0, 0]

print('Bem Vindo ao Banco do Povo')
acesso = input('Deseja acessar sua conta. s/n  ')

if acesso == 's':
    for i in range(3):    
        nome = input('Digite o Nome do titular da sua conta: ').lower()
        conta_ = int(input('Digite o Número da sua conta: '))

        if nome in login and conta_ in conta:
            index = login.index(nome)
            if conta[index] == conta_:
                print('Conta acessada com sucesso')
                print(f'Acesso à conta de {nome.capitalize()}, saldo: R$ {saldo[index]:.2f}')
                
                while True:
                    operacao = input('O que deseja acessar? Saldo | Deposito | Saque | Sair: ').lower()

                    if operacao == 'saldo':
                        print(f'Seu saldo atual é R$ {saldo[index]:.2f}')
                    elif operacao == 'deposito':
                        valor = float(input('Digite o valor a depositar: R$ '))
                        saldo[index] += valor
                        deposito[index] += valor
                        print(f'Você depositou R$ {valor:.2f}')
                    elif operacao == 'saque':
                        valor = float(input('Digite o valor a sacar: R$ '))
                        if valor > saldo[index]:
                            print('Saldo insuficiente.')
                        else:
                            saldo[index] -= valor
                            saque[index] += valor
                            print(f'Você sacou R$ {valor:.2f}')
                    elif operacao == 'sair':
                        print('Obrigado por usar o Banco do Povo! Até logo!')
                        break
                    else:
                        print('Opção inválida.')

                final = input('Deseja acessar o saldo da conta? s/n  ')
                if final == 's':
                    print(f'Seu saldo final é R$ {saldo[index]:.2f}')
                break  # Sai do for
            else:
                print('Número da conta não confere com o nome.')
        else:
            print('Nome ou número da conta incorretos!')

    else:
        print('Você atingiu o número máximo de tentativas. Conta bloqueada!')

input('Clique para Sair')
