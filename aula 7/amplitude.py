import statistics

dados = [1, 2, 3, 4, 5]
valor_maximo = max(dados)
valor_minimo = min(dados)
amplitude = valor_maximo - valor_minimo
print(f"Amplitude: {amplitude}")


frequencia = {1,2,3,5,6,4,3,2,1}
frequencia.sort()
print(frequencia)
amplitude = max(frequencia)- min(frequencia)
print(amplitude)


varianca = statistics.variance(frequencia)
print(varianca)



