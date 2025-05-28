quadri = []
qua0 = quadri.append(str(input('''Informe o nome e a pontuação da quadrilha
siga o exemplo (Raio de Sol – Pontuação: 97): ''')))
qua1 = quadri.append(str(input('''Informe o nome e a pontuação da quadrilha
siga o exemplo (Raio de Sol – Pontuação: 97): ''')))
qua2 = quadri.append(str(input('''Informe o nome e a pontuação da quadrilha
siga o exemplo (Raio de Sol – Pontuação: 97): ''')))
qua3 = quadri.append(str(input('''Informe o nome e a pontuação da quadrilha
siga o exemplo (Raio de Sol – Pontuação: 97): ''')))
qua4 = quadri.append(str(input('''Informe o nome e a pontuação da quadrilha
siga o exemplo (Raio de Sol – Pontuação: 97): ''')))
pont0 = (quadri[0])[-2] + (quadri[0])[-1]
pont1 = (quadri[1])[-2] + (quadri[1])[-1]
pont2 = (quadri[2])[-2] + (quadri[2])[-1]
pont3 = (quadri[3])[-2] + (quadri[3])[-1]
pont4 = (quadri[4])[-2] + (quadri[4])[-1]

if pont0 == '97':
    print('Campeã: {}'.format(quadri[0]))
if pont1 == '97':
    print('Campeã: {}'.format(quadri[1]))
if pont2 == '97':
    print('Campeã: {}'.format(quadri[2]))
if pont3 == '97':
    print('Campeã: {}'.format(quadri[3]))
if pont4 == '97':
    print('Campeã: {}'.format(quadri[4]))
