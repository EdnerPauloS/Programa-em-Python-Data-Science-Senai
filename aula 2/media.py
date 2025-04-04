notas = [[9.5,8.9,7],[8.5,9.5,5.6],[9.6,8.2,7.7],[5.9,8,7.5]]
nomes = ['Paulo', 'Daniel', 'Gustavo', 'Fabio']

media_p = sum(notas[0])/len(notas[0])
media_d = sum(notas[1])/len(notas[1])
media_g = sum(notas[2])/len(notas[2])
media_f = sum(notas[3])/len(notas[3])

print(f'Media aluno, {nomes[0]},media, {media_p:.2f}')
print(f'Media aluno, {nomes[1]},media, {media_d:.2f}')
print(f'Media aluno, {nomes[2]},media, {media_g:.2f}')
print(f'Media aluno, {nomes[3]},media, {media_f:.2f}')

lista_de_media = []
lista_de_media += (media_p,media_d, media_g,media_f)
maior =  max(lista_de_media)
print(f'Maior média, {maior:.2f}')
media_geral_classe = sum(lista_de_media)/len(lista_de_media)
print(f'Média geral, {media_geral_classe:.2f}')

         

