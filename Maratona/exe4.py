list_music = []
for i in range(1, 4):
    musicas = list_music.append(
        input('Informe a música {} para adicionar a lista: '.format(i)))
music = input('''Musicas já cadastradas.
Informe uma nova musica musica: ''')
if music in list_music:
    print('''As músicas cadastradas são
{}
{}
{}'''.format(list_music[0], list_music[1], list_music[2]))
else:
    print(list_music)
