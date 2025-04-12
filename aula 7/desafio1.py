import modulos

empresa1 = [2500, 2800, 3000, 9500, 12000]

empresa2 = [5000, 5200, 5300, 5400, 5500]

empresa3 = [1000, 2000, 8000, 15000, 20000]

empresa4 = [3500, 4000, 4200, 4300, 6000]

empresa5 = [1200, 1500, 1800, 2500, 10000]

print('Empresa 1')
print(f"Média da empresa 1: {modulos.media(empresa1):.2f}")
# Esta é a empresa que teve um inicio medio e um bom final
print(f"Médiana da empresa 1: {modulos.mediana(empresa1):.2f}")
# Esta é a empresa que teve a 2º pior mediana
print(f"Moda da empresa 1: {modulos.moda(empresa1):.2f}")
# Esta é a empresa que teve 3º melhor moda
print(f"O Desvio padrão da empresa 1: {modulos.desvio(empresa1):.2f}")
# Esta é a empresa que teve 2º desvio padrão mais alto
print(f"Amplitude: {modulos.amplitude(empresa1)}")
# Esta é a empresa teve a 2º melhor amplitude
print(f"Variância da empresa 1: {modulos.variancia(empresa1)}")
# Esta é a empresa teve a 2º melhor amplitude


print()
print('Empresa 2')
print(f"Média da empresa 2: {modulos.media(empresa2):.2f}")
# Esta é a empresa mais estavel
print(f"Médiana da empresa 2: {modulos.mediana(empresa2):.2f}")
# Esta é a empresa mais estavel com a 2º melhor mediana
print(f"Moda da empresa 2: {modulos.moda(empresa2):.2f}")
# Esta é a empresa mais estavel com a melhor moda
print(f"O Desvio padrão da empresa 2: {modulos.desvio(empresa2):.2f}")
# Esta é a empresa teve o menor desvio padrão
print(f"Amplitude: {modulos.amplitude(empresa2)}")
# Esta é a empresa teve a menor amplitude
print(f"Variância da empresa 2: {modulos.variancia(empresa2)}")
# Esta é a empresa teve a 2º melhor amplitude

print()
print('Empresa 3')
print(f"Média da empresa 3: {modulos.media(empresa3):.2f}")
# Esta é a empresa que mais evoluio com o tempo
print(f"Médiana da empresa 3: {modulos.mediana(empresa3):.2f}")
# Esta é a empresa que tem a melhor mediana
print(f"Moda da empresa 3: {modulos.moda(empresa3):.2f}")
# Esta é a empresa que teve a pior moda
print(f"O Desvio padrão da empresa 3: {modulos.desvio(empresa3):.2f}")
# Esta é a empresa que teve o maior desvio padrão
print(f"Amplitude: {modulos.amplitude(empresa3)}")
# Esta é a empresa teve a melhor amplitude
print(f"Variância da empresa 3: {modulos.variancia(empresa3)}")
# Esta é a empresa teve a 2º melhor amplitude
print()

print('Empresa 4')
print(f"Média da empresa 4: {modulos.media(empresa4):.2f}")
# Esta é a empresa 2º empresa mais estavel
print(f"Médiana da empresa 4: {modulos.mediana(empresa4):.2f}")
# Esta é a empresa 3º empresa com uma boa mediana
print(f"Moda da empresa 4: {modulos.moda(empresa4):.2f}")
# Esta é a empresa 2º melhor moda
print(f"O Desvio padrão da empresa 4: {modulos.desvio(empresa4):.2f}")
# Esta é a empresa teve o 2º menor desvio padrão
print(f"Amplitude: {modulos.amplitude(empresa4)}")
# Esta é a empresa teve a penultima amplitude
print(f"Variância da empresa 4: {modulos.variancia(empresa4)}")
# Esta é a empresa teve a 2º melhor amplitude

print()
print('Empresa 5')
print(f"Média da empresa 5: {modulos.media(empresa5):.2f}")
# Esta é a empresa que menos evoluio com o tempo
print(f"Médiana da empresa 5: {modulos.mediana(empresa5):.2f}")
# Esta é a empresa que menos evoluio com a pior mediana 
print(f"Moda da empresa 5: {modulos.moda(empresa5):.2f}")
# Esta é a empresa ficou em 4º na moda
print(f"O Desvio padrão da empresa 5: {modulos.desvio(empresa5):.2f}")
# Esta é a empresa ficou em 3º desvio padrão bem no meio
print(f"Amplitude: {modulos.amplitude(empresa5)}")
# Esta é a empresa teve a 3º amplitude
print(f"Variância da empresa 5: {modulos.variancia(empresa5)}")
# Esta é a empresa teve a 2º melhor amplitude


