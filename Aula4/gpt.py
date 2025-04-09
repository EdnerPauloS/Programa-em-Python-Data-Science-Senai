conta = {
    'Paulo' : [1, 3000.00],
    'Daniel': [2, 1500.00],
    'Felipe': [3, 4000.00],
    'Gustavo': [4, 1000.00],
}

# - Acesso a conta
print('Bem Vindo ao Banco do Povo')
acesso = input('Deseja acessar sua conta? s/n: ')

if acesso == 's':
    for i in range(3):  # Permite até 3 tentativas de acesso
        nome = input('Digite o Nome do titular da sua conta: ')
        conta_ = int(input('Digite o Número da sua conta: '))  # Convertemos para inteiro para comparação

        # Verificar se o nome está no dicionário e se o número da conta corresponde
        if nome in conta and conta_ == conta[nome]['']:  # Comparando o número da conta
            print(f'Conta acessada com sucesso! O saldo atual de {nome} é: R$ {conta[nome][1]:.2f}')
            print('O que deseja acessar?')
            
            resultado = input('Saldo | Depósito | Saque | Sair: ')
            break  # Se o login for bem-sucedido, sai do loop
        else:
            print('Nome ou número da conta incorretos!')
    else:
        print('Você atingiu o número máximo de tentativas. Conta bloqueada!')
        
# Função para ver o extrato
def ver_extrato(nome):
    print(f'Extrato de {nome}:')
    print(f'Saldo atual: R$ {conta[nome][1]:.2f}')

# Função para fazer depósito
def deposito(nome, valor):
    conta[nome][1] += valor
    print(f'Depósito de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {conta[nome][1]:.2f}')

# Função para fazer saque
def saque(nome, valor):
    if valor <= conta[nome][1]:
        conta[nome][1] -= valor
        print(f'Saque de R$ {valor:.2f} realizado com sucesso. Novo saldo: R$ {conta[nome][1]:.2f}')
    else:
        print('Saldo insuficiente para o saque.')

# Menu de operações após o login
if acesso == 's' and nome in conta:
    while True:
        resultado = input('O que deseja acessar? (Saldo | Depósito | Saque | Sair): ').lower()
        
        if resultado == 'saldo':
            ver_extrato(nome)
        elif resultado == 'deposito':
            valor_deposito = float(input('Digite o valor do depósito: R$ '))
            deposito(nome, valor_deposito)
        elif resultado == 'saque':
            valor_saque = float(input('Digite o valor do saque: R$ '))
            saque(nome, valor_saque)
        elif resultado == 'sair':
            print('Saindo do sistema. Obrigado por usar o Banco do Povo!')
            break
        else:
            print('Opção inválida. Tente novamente.')
