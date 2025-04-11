import statistics

def moda(freque):
    f= statistics.mode(freque)
    return f

def mediana(freque):
    f= statistics.median(freque)
    return f

def media(freque):
    f= statistics.mean(freque)
    return f