import modulo


f = {1,2,3,6,4}

media1 = modulo.media(f)
mediana1 = modulo.mediana(f)
moda1 = modulo.moda(f)

print(f'''
MEDIA - {media1}
MEDIANA - {mediana1}
MODA - {moda1}
''')

f2 = [1.5,6.8,9.7,10.6]

media2 = modulo.media(f2)
mediana2 = modulo.mediana(f2)
moda2 = modulo.moda(f2)

print(f'''
MEDIA - {media2}
MEDIANA - {mediana2}
MODA - {moda2}
''')

f3 = [200,300,500,700,900,400,600]

media3 = modulo.media(f3)
mediana3 = modulo.mediana(f3)
moda3 = modulo.moda(f3)

print(f'''
MEDIA - {media3}
MEDIANA - {mediana3}
MODA - {moda3}
''')