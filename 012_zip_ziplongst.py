"""
zip - unindo iteráveis
zip_longest - Itertools
"""
from itertools import zip_longest, count



# Código zip pega a menor.
cidades = ['São Paulo', 'Salvador', 'Bahia', 'Rio de Janeiro']

# Código:
estados = ['SP', 'MG', 'BA', 'RJ']

cidades_estados = zip(estados, cidades)


for valor in cidades_estados:
    print(valor)

print('\U0001f150'*40)

# Código zip_longst pega a maior lista e completa com none.
cid1 = ['São Paulo', 'Salvador', 'Bahia', 'Rio de Janeiro', 'Alagoas', 'Outra']

# Código:

est1 = ['SP', 'MG', 'BA', 'RJ']

cidades_estados = zip_longest(est1, cid1, fillvalue='estado')

print(list(cidades_estados))

print('\U0001f150'*40)

indice = count()
cid2 = ['São Paulo', 'Salvador', 'Bahia', 'Rio de Janeiro', 'Alagoas', 'Outra']
est2 = ['SP', 'MG', 'BA', 'RJ']

cid2_estados = zip(indice, est2, cid2)

for indice, est2, cid2 in cid2_estados:
    print(indice, est2, cid2)














