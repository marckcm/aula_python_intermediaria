import sys
import time
"""
iteraveis, iteradores e geradores
"""

lista = [0, 1, 2, 3, 4, 5, 6]
lista = iter(lista)                     # Modifica a lista para Iteravel
lista2 = "string"

print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print(next(lista))
print('\U0001f120'*20)

print(hasattr(lista2, '__iter__'))      # "hasattr" checa se o objeto iteravel junto com "__iter__"
print('\U0001f120'*20)

for v in lista2:
    print(v)
print('\U0001f120'*20)

print(hasattr(lista, '__next__'))
print('\U0001f120'*20)

lista3 = list(range(10))
print(lista3)
print(sys.getsizeof(lista3))
print('\U0001f120'*20)


def gera():
    # r = []
    for n in range(100):
        # r.append(n)
        yield n
        time.sleep(0.1)
    # return r


g = gera()
print(hasattr(g, "__next__"))


# for v in g:
#     print(v)
print('\U0001f120'*20)


def gera2():
    variavel = 'Valor 1'
    yield variavel
    variavel = 'Valor 2'
    yield variavel
    variavel = 'Valor 3'
    yield variavel


g = gera2()
# print(next(g))
# print(next(g))
# print(next(g))

for item in g:
    print(item)
