# https://www.modular.com/mojo


def v_horas(quant_horas,salario):
    dado = salario/quant_horas
    return round(dado,2)


def hora_extra(valor_extra, dado):
    extra = valor_extra * dado
    return extra


salario  =  float(input('salario: '))
carga =  float(input('carga : '))
valor_hora  = v_horas(carga,salario)
horas_extra = hora_extra(1.5,valor_hora)
print('Hora do colaborador - ', valor_hora)
print('Hora extra do colaborador, ', round(horas_extra,2))






# def calculo(lista,dado):
#     for i in range(1,5):
#        lista.append(dado)
#        print(lista)
    


# LISTA = []
# DADO = input('>>')
# calculo(LISTA,DADO)



        


# print(calculo(1.71,65))
# print(calculo(1.81,70))
# print(calculo(1.50,65))
# print(calculo(1.70,65))




# a = True


# def teste():
#     global t, x
#     t = 10
#     x = 20
#     print(t,x)
# teste()
# print(t)

def sub(a,b):
    return a - b


def soma(a,b):
    return a + b


def mult(a,b):
    return a * b


def div(a,b):
    return a / b




def calculadora():
 while True:    
    n1 = float(input('>>'))
    op = input('Escolha a operação = +|-|*|/')
    if op == '+':
        n2 = float(input('>>'))
        print(soma(n1,n2))
        
    elif op == '-':
        n2 = float(input('>>'))
        print(sub(n1,n2))  
                  
    elif op == '*':
        n2 = float(input('>>'))
        print(mult(n1,n2))  


    elif op == '/':
        n2 = float(input('>>'))
        print(div(n1,n2))  
                          


calculadora()                  