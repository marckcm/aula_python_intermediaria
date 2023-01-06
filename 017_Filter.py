"""
filter = filtra os dados de uma coluna
"""

from dados import produtos, pessoas, lista

nova_lista = filter(lambda x: x > 5, lista)
nova_lista2 = [x for x in lista if x > 5]
print(nova_lista2)
print(list(nova_lista))

print('\U0001f520'*20, '\n')

tab_preco = filter(lambda pr: pr['preco'] > 1000, produtos)

for item in tab_preco:
    print(item)

print('\U0001f520'*20, '\n')


def filtra(produto):
    if produto['preco'] > 50:
        produto['ta_caro'] = True
        return True


tab_preco2 = filter(filtra, produtos)

for i in tab_preco2:
    print(i)

print('\U0001f520'*20, '\n')


def maior_id(pessoa):
    if pessoa['idade'] >= 18:
        return True
    else:
        return False


list_id = filter(maior_id, pessoas)

for p in list_id:
    print(p)
