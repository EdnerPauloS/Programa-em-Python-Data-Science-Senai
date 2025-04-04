print('Digite o seu nome; ')#-> Função de imprime um dado
usuario = input() #-> Função que solicita a entrada de um dado
print('Digite o seu Sobrenome; ')#-> Função de imprime um dado
nome = input() #-> Função que solicita a entrada de um dado
print('Digite sua idade; ')#-> Função de imprime um dado
idade =(input()) #> Função que solicita a entrada de um dado
print('Digite sua endereço; ')#> Função de imprime um dado
endereço = input() #> Função que solicita a entrada de um dado
print('Digite uma senha; ')#> Função de imprime um dado
senha = input()
print(f'O seu nome é {usuario} {nome} tem a idade de {idade} anos e mora na Rua {endereço} e foi cadastrado com sucesso ')#> Função de imprime todos os dados lancados menos a senha

while True:
    print('Deseja entrar no sistema. s/n')# Função para loop de login
    entre = input()


    if entre == 's':# se 's' continua
        usuario0 = input('Qual o seu usuario: ')
        senha0 =    input('Qual sua senha: ')
        if usuario == usuario0 and senha == senha0:# se usuario e senha forem corretas ok
            print('Login Feito com sucesso')
            print('Boa diversao')
            break
        elif usuario != usuario0 and senha == senha0:# se usuario errado nao loga
            print('Seu usuario esta incorreta, e a sua senha esta correta')
            print(senha)
        elif usuario == usuario0 and senha != senha0:# se senha forem incorretas não loga
            print('Seu usuario esta correta, e a sua senha esta incorreta')
            print(usuario)
        else:# se usuario e senha forem incorretas ir para loop
            print('Seu usuario e sua senha estao incorretas')
            print(usuario0 , senha0)
            
    else:# se qualquer outra coisa sai do sistema
        print('Voce saio do sistema')    
    print('Voce gostaria de voltar ao Sistema. s/n')
    entre1 = input()
    if entre != 's':
       break

input()
   
#VAMOS RECORDAR: 

# 1 - Crie um script que solicite ao usuario, idade, endereço, nome, mostre no console
# 2 - Crie um script que solicite ao usuário a senha em seguida mostre no console
# 3 - Crie um script que solicite ao usuario o nome e em seguida crie outro que solicite 
# o sobrenome, concatene e em seguida mostre no console.  