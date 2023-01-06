"""
Agrupando Valores
groupby -
tee
"""
from itertools import groupby, tee

alunos = [
    {'nome': 'joão', 'nota': 'A'},
    {'nome': 'Andre', 'nota': 'B'},
    {'nome': 'Leticia', 'nota': 'C'},
    {'nome': 'Marcos', 'nota': 'A'},
    {'nome': 'Eli', 'nota': 'A'},
    {'nome': 'Roberto', 'nota': 'B'},
    {'nome': 'Jussara', 'nota': 'D'},
    {'nome': 'Bento', 'nota': 'D'},
    {'nome': 'Ananias', 'nota': 'A'},
    {'nome': 'Geronimo', 'nota': 'B'},
    {'nome': 'Fernando', 'nota': 'C'},

]

alunos.sort(key=lambda item: item['nota'])
for i in alunos:
    print(i)
alunos_agrupados = groupby(alunos, lambda item: item['nota'])

print('\n', '\U0001f250'*20, '\n')

for agrupamento, valores_agrupados in alunos_agrupados:
    var1, var2 = tee(valores_agrupados)

    print(f'Agrupamento: {agrupamento}')

    for aluno in var1:
        print(f'\t{aluno}')
    print()

    quantidade = len(list(var2))
    print(f'\t{quantidade} alunos tiraram a nota {agrupamento}')
    print()
