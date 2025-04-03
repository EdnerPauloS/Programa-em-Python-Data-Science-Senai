import funcoes


peso = float(input('Informe quantos quilos você Pesa: '))
altura = float(input('Informe quanto você tem de altura: '))


imc = funcoes.calcular_imc(peso, altura)
classificacao = funcoes.classificar_imc(imc)

print(f'\nVocê pesa {peso} kg e tem {altura}m de altura.')
print(f'Seu Índice de Massa Corporal (IMC) é {imc:.2f}')
print(f'Classificação: {classificacao}')
