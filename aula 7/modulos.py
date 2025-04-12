import numpy as np
from statistics import *
import math


def media(tupla):
    media = sum(tupla) / len(tupla)
    return media

def mediana(tupla):
    tupla.sort()
    n = len(tupla)
    mediana = (tupla[n // 2] if n % 2 != 0 else (tupla[n // 2 - 1] + tupla[n // 2]) / 2)
    return mediana

def moda(tupla):
    return mode(tupla)

def desvio(tupla):
    media = sum(tupla) / len(tupla)
    soma_quadrados = sum((x - media) ** 2 for x in tupla)
    desvio = math.sqrt(soma_quadrados / len(tupla))
    return desvio

def amplitude(tupla):
    valor_maximo = max(tupla)
    valor_minimo = min(tupla)
    amplitude = valor_maximo - valor_minimo
    return amplitude

def variancia(tupla):
    return np.var(tupla)