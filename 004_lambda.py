"""
função lambda

cria uma função igual ao def
"""

def func(arg, arg2):
    return arg*arg2


var = func(2, 2)
print(var)

a = lambda x, y: x * y

print(a(2, 2))


lista = [
    ['p1', 13],
    ['p2', 206 ],
    ['p3', 20],
    ['p4', 1350]
]


# def func(item):
#     return item[1]
#
#
# lista.sort(key=func)            # coloca a lista em ordem numerica
# print(lista)
# lista.sort(key=func, reverse=True)          # inverte a ordem da lista maior para o menor
# print(lista)


lista.sort(key=lambda item: item[1], reverse=True)
print(lista)

print(sorted(lista, key=lambda i: i[0], reverse=True))