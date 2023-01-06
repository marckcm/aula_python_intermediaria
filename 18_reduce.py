"""
reduce = acumula valores
"""
from dados import produtos, pessoas, lista
from functools import reduce

acumula = 0
for i in lista:
    acumula += i
print(acumula)

print(1+2+3+4+5+6+7+8+9+10)

soma_lista = reduce(lambda acu, i: i + acu, lista, 0)
print(soma_lista)

print('\U0001f510'*20)

soma_precos = reduce(lambda soma, p: p['preco'] + soma, produtos, 0)
print(f'A soma dos dados em pessoas e de R$ {soma_precos:.2f}')

media = soma_precos / len(produtos)
print(f'e a media dos valores é de R$ {media:.2f}')

print('\U0001f510'*20)

# Media de idade

soma_id = reduce(lambda soma, id: id["idade"] + soma, pessoas, 0)
id_media = soma_id / len(pessoas)
print(f'A idade media das pessoas nos\n dados é de {id_media:.0f} anos ')


