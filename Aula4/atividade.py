# Crie um sistema de banco, com as seguintes operações:

# SISTEMA DE BANCO 
conta = {
    'Paulo' : 1,
    'Daniel': 2,
    'Felipe': 3,
    'Gustavo':4
      
}
saldo = [3000,1500,4000,1000]

# - Acesso a conta
print('Bem Vindo ao Banco do Povo')
acesso = input('Deseja acessar sua conta. s/n  ')
if acesso == 's':
    for i in range(3):    
        nome = input('Digite o Nome do titular da sua conta:  ')
        conta_ = int(input('Digite o Número da sua conta:  '))
        if nome == conta[nome] and conta_ == conta[nome]:
            print('Conta acessada com sucesso')
            print(f'Acesso a conta de {nome} e tem o saldo de {conta[nome][1]:.2f}')
            print('Oque deseja acessar')
            
            resultado = input('Saldo | Deposito | Saque | Sair')
            break
        else:
            print('Nome ou número da conta incorretos!')
    else:
        print('Você atingiu o número maximo de tentativas. Conta Bloquiada!')
            
    
            


# - Ver extrato
# - Fazer um deposito
# - Fazer um saque 
# - Sair do sistema 
# - Ao finalizar seu sistema adicione: