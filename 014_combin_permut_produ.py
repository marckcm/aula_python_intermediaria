"""
Combination, Permutations e Product - itertools
combinação:
Permutação:
Ambos não repetem valores unicos
Produto - Ordem importa e repete valores únicos.
video 27
https://drive.google.com/drive/folders/1qUALwtScIGRsj62nntvXIrcjlL6lcJYj
"""
from itertools import combinations, permutations, product

times = ['Flamengo', 'Botafogo', 'Vasco', 'Fluminense', 'São Paulo', 'Corintians']

# Todos ja terão jogados entre eles no final.
for jogos in combinations(times, 2):
    print(jogos)

print('\U0001f120'*40)

# Caso você precise que cada um precise ter trocado entre eles usa o Permutations.

verba = ['Nação', 'Capitais', 'estados', 'População']
for dinheiro in permutations(verba, 2):
    print(dinheiro)     # Resumindo o dinheiro está passando entre eles
                        # em constante movimento tudo que sai retorna e no final a população
                        # devolve com juros do trabalho exercido

print('\U0001f120'*40)

# product é um item que pode ser usado para combinações possiveis entre numeros
# ex senha com números de 1 a 4 de 2 dígitos
porta = [1, 2, 3, 4]
for combinacao in product(porta, repeat=2):
    print(combinacao)

