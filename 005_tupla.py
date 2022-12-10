"""
Igual a lista mais não pode ser modificada
"""
t1 = (1, 2, 3, 'casa', 'indice')

print(type(t1))

for v in t1:
    print(v)

t1 = 1,2,3,4,5,6
t2 = 10,20,30,40,50,60
t3 = t1 + t2

print(t3)

n1, n2, n3, *_, n11 = t3
print(n11)

# Para editar uma tupla tem que passar ela para lista primeito

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
tupla = list(tupla)
tupla[1] = "marcelo"
print(tupla, type(tupla))

# alterando novamente para tupla

tupla = tuple(tupla)
print(tupla, type(tupla))






