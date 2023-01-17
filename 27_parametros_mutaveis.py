"""
Problemas dos parâmetros mutáveis nas funções
"""


# É alertado que o argumento da função é mutável tudo que colocar vai se extender a lista
def lista_de_clientes(lista_clientes, lista=[]):
    lista.extend(lista_clientes)
    return lista


# junta todas as listas em uma se imprimir elas separadas dara a mesma lista
clientes1 = lista_de_clientes(['edvaldo', 'joão', 'raquel', 'Renata', 'leo', 'vaguinho'])
clientes2 = lista_de_clientes(['marcos', 'jonas', 'vitor'])
clientes3 = lista_de_clientes(['adriana'])

print(clientes1)
print(clientes2)
print(clientes3)

print('\U0001f501' * 30)


# Resolvendo o problema
def lista_de_clientes2(lista_clientes, lista=None):
    if lista is None:
        lista = []
    lista.extend(lista_clientes)
    return lista


clientes1 = lista_de_clientes2(['edvaldo', 'joão', 'raquel', 'Renata', 'leo', 'vaguinho'])
clientes2 = lista_de_clientes2(['marcos', 'jonas', 'vitor'])
clientes3 = lista_de_clientes2(['adriana'])

print(clientes1)
print(clientes2)
print(clientes3)
