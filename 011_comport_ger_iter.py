"""
Comportamento de geradores e iteradores:

São feitos para você consumir o valor deles
depois de consumidos eles se esgotam.
Para consumir os iteradores e geradores tem que ser
utilizado um outro recurso sera abordado mais a frente
"""

nome = 'marcelo esta aqui'

for letra in nome:
    print(letra)

print('\U0001f200' * 20, '1')

for letra in nome:
    print(letra)
# uma string lista ou tuplas podem ser chamadas varias vezes

print('\U0001f200' * 20, '2')

iterador = iter(nome)  # Passando string para iteravel

try:
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
    # print(next(iterador))
except:
    pass

print('restante do iterador não consumido')

for valor in iterador:
    print(valor)

print('\U0001f200' * 20, '3')

gerador = (letra for letra in nome)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))

print('olha o FOR')

for letra in gerador:
    print(letra)

print('olha o segundo FOR')
# não tem mais nada a ser consumido então para a iteração
# o for abaixo não retoma o gerador novamente
for letra in gerador:
    print(letra)

print(next(gerador))  # Vai dar erro pois não tem mais letras para consumir
