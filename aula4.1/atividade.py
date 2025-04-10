# Crie um sistema de banco, com as seguintes operações:

# SISTEMA DE BANCO 
conta = [1,2,3,4]
login = ['Paulo' ,'Daniel','Felipe','Gustavo']
saldo = [3000,1500,4000,1000]
deposito =[0,0,0,0]
saque = [0,0,0,0]
# - Acesso a conta
print('Bem Vindo ao Banco do Povo')
acesso = input('Deseja acessar sua conta. s/n  ')
if acesso == 's':
    for i in range(3):    
        nome = input('Digite o Nome do titular da sua conta:  ')
        conta_ = int(input('Digite o Número da sua conta:  '))
        if nome == login and conta_ == conta:
            print('Conta acessada com sucesso')
            print(f'Acesso a conta de {nome} e tem o saldo de {saldo:.2f}')
            print('Oque deseja acessar')            
            operacao = input('Saldo | Deposito | Saque | Sair')

        elif operacao == 'Saldo':
            print(f'O seu saldo atual e {saldo}')    
        elif operacao == 'Deposito':
            deposito = saldo + deposito
            print(f'Voce depositou {deposito} ')    
        elif operacao == 'Saque':
            saque = saldo + saque
            print(f'Voce sacou {saque} ')    
        elif operacao == 'sair':
            print('Obrigado por usar o Banco do Povo! Até logo!')    
            break
        else:
            print('Nome ou número da conta incorretos!')
        final= input('Deseja acessar o saldo atual da  conta. s/n  ')
        if final == 's':
            saldo_final = saldo - saque or saldo + deposito
            print(f'Seu saldo atual é {saldo_final}')
    else:
        print('Você atingiu o número maximo de tentativas. Conta Bloquiada!')
            
    
            


# - Ver extrato
# - Fazer um deposito
# - Fazer um saque 
# - Sair do sistema 
# - Ao finalizar seu sistema adicione: