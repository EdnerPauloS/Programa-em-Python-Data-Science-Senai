import statistics as sts


d = {
'empresa1' : [2500, 2800, 3000, 9500, 12000],
'empresa2' : [5000, 5200, 5300, 5400, 5500],
'empresa3' : [1000, 2000, 8000, 15000, 20000],
'empresa4' : [3500, 4000, 4200, 4300, 6000],
'empresa5' : [1200, 1500, 1800, 2500, 10000],
}



def estatistica():
    dados_ = [y for y in d.keys() ]
    empresa1 = dados_[0]
    dados = [y for y in d.values()]
    moda = sts.mode(dados[0])
    print(empresa1,moda)


        # moda = sts.mode(dicionario[c])
        # media = sts.mean(dicionario[c])
        # mediana = sts.median(dicionario[c])
        # des = sts.stdev(dicionario[c])
        # print(f'''ESTATISTICA
              
        #       MEDIA {media}
        #       MODA {moda}
        #       MEDIANA {mediana}
        #       DESVIO {des}
              
        #       ''')


estatistica(d)







# s =  input('Digite sim para continuar: ')
# while s == 'sim':
#     nome = input('Digite nome:')
#     n1 = int(input('Digite dado: '))
#     n2 = int(input('Digite dado: '))
#     n3 = int(input('Digite dado: '))
#     d[nome] = [n1,n2,n3]
#     s =  input('Digite sim para continuar: ')