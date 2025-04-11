frequencia  =  [1,2,3,6,4]
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

frequencia1  = [1.5,6.8,9.7,10.6]
conj = set(frequencia1)
if len(conj) == len(frequencia1):
    print('Não sem moda')
else:
    moda  =  max(conj, key=frequencia1.count)
    print(moda)


    print('Tem moda')

media  = sum(frequencia1) / len(frequencia1)
print('Media ', media)


tamanho  =  len(frequencia1)
if tamanho % 2 == 1:
    print('mediana:',frequencia1[2:3])
else:
    n1 = frequencia1[2]
    n2 = frequencia1[3]
    soma = n1 + n2/2
    print('Mediana', soma)