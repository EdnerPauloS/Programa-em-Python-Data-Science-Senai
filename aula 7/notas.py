import meu_modulo as md



#  SISTEMA DEVE GERENCIAR AS NOTAS DOS ESTUDANTES, 
# APRESENTANDO ESTATÍSTICAS COMO MODA, MÉDIA, MEDIANA, 
# AMPLITUDE DESVIO PADRÃO. ALÉM DISSO, DEVE IDENTIFICAR 
# A MENOR E A MAIOR NOTA. ORGANIZE O CÓDIGO EM MÓDULOS 
# E SEPARE AS FUNCIONALIDADES EM FUNÇÕES DISTINTAS.


dicionario = {}


def calcular_notas():
    
    for n in range(1,3):
        nome = input('Nome:')
        n1 = float(input('nota1'))
        n2 = float(input('nota1'))
        dicionario[nome]  = [n1,n2]
        print(dicionario)
        md.moda(dicionario[nome])
        md.media(dicionario[nome])
        md.mediana(dicionario[nome])
        md.amplitude(dicionario[nome])
        md.devio(dicionario[nome])    


calcular_notas()
    