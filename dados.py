import math

produtos = [
    {'nome': 'p1', 'preco': 15.00},
    {'nome': 'p2', 'preco': 125.10},
    {'nome': 'p3', 'preco': 135.00},
    {'nome': 'p4', 'preco': 10.00},
    {'nome': 'p5', 'preco': 115.00},
    {'nome': 'p6', 'preco': 18.00},
    {'nome': 'p7', 'preco': 1335.00},
    {'nome': 'p8', 'preco': 1455.00},
    {'nome': 'p9', 'preco': 115.00},
    {'nome': 'p10', 'preco': 1505.00},
    {'nome': 'p11', 'preco': 151.00},
]

pessoas = [
    {'nome': 'jose', 'idade': 18},
    {'nome': 'ednaldo', 'idade': 42},
    {'nome': 'antonio', 'idade': 18},
    {'nome': 'felipe', 'idade': 12},
    {'nome': 'ednaldo', 'idade': 13},
    {'nome': 'moises', 'idade': 45},
    {'nome': 'pedro', 'idade': 60},
    {'nome': 'carlos', 'idade': 15},
    {'nome': 'leticia', 'idade': 43},
    {'nome': 'pricila', 'idade': 39},
    {'nome': 'robson', 'idade': 50},
    {'nome': 'ednaldo', 'idade': 27},
    {'nome': 'leandro', 'idade': 29},
    {'nome': 'aline', 'idade': 71},
]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

PI = math.pi


def dobra(lista):
    return [x*2 for x in lista]


def soma(lista):
    n = 1
    for i in lista:
        n += i
    return n


def multiplica(lista):
    r = 1
    for i in lista:
        r *= i
    return r


if __name__ == '__main__':
    print(dobra(lista))
    print(multiplica(lista))
    print(PI)
