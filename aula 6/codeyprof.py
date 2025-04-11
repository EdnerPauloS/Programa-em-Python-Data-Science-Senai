
# COM  -  python puro


frequencia  =  [3,2,5,7,6,8,8]
conj = set(frequencia)
if len(conj) == len(frequencia):
    print('Não sem moda')
else:
    moda  =  max(conj, key=frequencia.count)
    print(moda)


    print('Tem moda')




media  = sum(frequencia) / len(frequencia)
print('Media ', media)



tamanho  =  len(frequencia)
if tamanho % 2 == 1:
    print('mediana:',frequencia[2:3])
else:
    n1 = frequencia[2]
    n2 = frequencia[3]
    soma = n1 + n2/2
    print('Mediana', soma)





