import numpy as np
#Desafio 1:
array_sequencia = np.arange(20)
print(array_sequencia)
print(array_sequencia[0:5])  
print(array_sequencia[15:])  
print(array_sequencia[4:10])
print("\n")
#Desafio 2:
numeros = np.random.randint(1,10, (2,3,3))

print(numeros*numeros)
print(np.prod(numeros)) 