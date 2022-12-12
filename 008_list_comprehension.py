"""
list comprehension python
Constroi uma lista mais rápida


"""

l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
ex1 = [variavel for variavel in l1]
ex2 = [v * 2 for v in l1]
ex3 = [(v, v2) for v in l1 for v2 in range(3)]
print(ex1)
print(ex2)
print(ex3)
print('\U0001f301' * 40)

l2 = ['marcelo', 'adriana', 'letras']
ex4 = [v.replace('a', '@').upper() for v in l2]         # replace troca e upper deicha em maiúsculo.
print(ex4)
print('\U0001f301' * 40)

tupla = (
    ('chave', 'valor'),
    ('chave2', 'valor2')
)
ex5 = [(y, x) for x, y in tupla]        # Inverte a Tupla
ex5 = dict(ex5)
print(ex5)
print('\U0001f301' * 40)

l3 = list(range(50))
ex6 = [v for v in l3 if v % 3 == 0 if v % 8 == 0]
print(ex6)
print('\U0001f301' * 40)

ex7 = [v if v % 3 == 0 and v % 8 == 0 else 0 for v in l3]
print(ex7)
