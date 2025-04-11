import random


# ***1 - Com funções crie um sistema de médias.***


# def media1(lista):
#     media = sum(lista)/len(lista)
#     return media


# def media2(nome_aluno):
#     dados1 = {
#     'João':[1,2,3,6,5,9],
#     'Karla':[1,2,3,6,6,7],
#     'Fernanda':[1,2,3,6,9,9]
#     }
#     notas =  dados1[nome_aluno]
#     print(notas)
#     media = sum(notas)/len(dados1[nome_aluno])
#     return media






# print(media2('Fernanda'))
# print(media2('Karla'))
# print(media2('João'))


# lista_notas  =  [10,5,3,6,9,9,9,9]
# print(media1(lista_notas))




# ***2 - Com funções crie um sistema de para 
# calcular o IMC***



# def imc(peso, altura):
#     altura =  float(input('Altura: '))
#     imc = peso/(altura**2)
#     print(f'{round(imc,21.)}')


    
# imc(70,1.65)




# ***3 - Com funções crie um jogo da adivinhação***

def advinha(chute):
    c = [3,2,1]
    for n in c:


        print('Vc tem ', n, 'chances')
        chute  = int(input('Inteiro'))
        aleatorio = random.randint(1,11)
        if chute  == aleatorio:
            print('Acertou em cheio o nº é:', aleatorio)
            break
        else: 
            print('Erro, nº é: ', aleatorio)
            print('Essa foi a chance ', n) 
    print('Suas chances esgotaram', n)



advinha(9)