"""
Funções (def) em Python  - *args **kwargs -
"""


def fun_1(a1, a2, a3, nome=None, a5=None):
    print(a1, a2, a3, nome, a5)
    return nome, a5
var_1 = fun_1(1, 1, 1, nome='marcelo', a5=2)
print(var_1[0], var_1[1])

print(' \U0001f319'*20)


def fun(*args, **kwargs):
    print(args)
    print(args[0])
    print(args[-1])
    print(len(args))
    print(kwargs)


fun(1, 2, 3, 4, 5, 6)

lista = [1, 2, 3, 4, 5]
lista_2 = [10, 20, 30, 40, 50]
fun(*lista, *lista_2, nome='marcelo', sobrenome='castro')


