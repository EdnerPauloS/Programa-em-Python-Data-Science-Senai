def calcular_imc(peso,altura):
    return peso / (altura** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return ('Abaixo do Peso')
    elif imc >= 18.5 and imc < 24.9:
        return ('Peso Normal')
    elif imc >= 25 and imc < 29.9:
        return ('Possível Sobrepeso')
    elif imc >= 30 and imc < 34.9:
        return ('Obesidade grau 1')
    elif imc >= 35 and  imc < 39.9: 
        return ('Obesidade grau 2')
    else: #  imc >= 40:
        return ('Obesidade grau 3. Também chamada de Obesidade Mórbida')
    