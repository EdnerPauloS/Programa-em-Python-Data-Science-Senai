import statistics 


def moda(lista):
    moda1 = statistics.mode(lista)
    print('moda',moda1)


def mediana(lista):
    mediana1 = statistics.median(lista)
    print('mediana',mediana1)


def media(lista):
    media1 = statistics.mean(lista)
    print('media',media1)


def devio(lista):
    desvio1 = statistics.stdev(lista)
    print('Desvio',desvio1)        


def amplitude(lista):
    amplitude1 = max(lista) - min(lista)
    print('amplitude',amplitude1) 