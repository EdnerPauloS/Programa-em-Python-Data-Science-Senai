import num as np


lista = [1,2,3,6,4]
ar = np.array(lista)
print(ar)

# função zeros  

zeros =  np.zeros(10)
print(zeros)


# função ones

uns = np.ones(10)
print(uns)

# arange()

sequencia  = np.arange(0,10,2)
print(sequencia)


# lineares


lineares = np.linspace(0,10)
print(lineares)



# exemplo calculos arimeticos

a = np.array([1,2,3,5])
b = np.array([1,2,3,6])

# raiz 
print(np.sqrt(a))
print(np.sin(a))
print(np.exp(a))


# estatistica 


print(np.mean(a))
print(np.var(a))
print(np.std(a))

# range
ar = np.arange(100).reshape((5,10,2))
print(ar)

# min
soma  =  np.min(a)
print(soma)


# slice
a = np.array([1,2,3,5,20,21,25,30])
fatia  =  a[3]
print(fatia)


# filtro
filtro = a > 10
print(a[filtro])

# concatenar 
juntar =  np.concatenate((a,b))
print(juntar)

# l = [1,2,6]
# te = round(l)
# print(te)


# round

ar = np.array([1.10,2.5,336.25,6.5,5,6])
teste  =  np.round(ar)
print(teste)

# filtro = np.arange(0,3,-1)
a = np.array(['a','b','c'])
b = np.array(['a','b','c'])
aleatorio  =  np.random.choice(a)
print(aleatorio) 


# vetores avançados
ar  =  np.array([1,2,3,6,10,20,30,40])
x =  ar [ar % 2 == 0] 
print(x)


# dir serve para descobrir os métodos para aquele 
# objeto
ar = np.array([1,2,3,6])
funct = dir(ar)
print(funct)