"""
add (adiciona), update(atualiza), clear, discard
union | (une)
intersection & (todos elementos presentes nos dois sets)
symmetric _diference ^ (Elementos que estão nos dois sets, mas não em ambos)
"""

ex = {1, 2, 3}

for item in ex:
    print(item)

print('\U0001f315'*40)

n_exe = set()           # Para criar um set vazio se colocar {} vai identificar como dicionário.
n_exe.add(2)            # Adiciona um elemento
n_exe.add(6)            # Remove um elemento
n_exe.discard(2)
print(n_exe)
n_exe.update('string', [1,3,4], {9,8,7}, [2,5,0])      # Coloca todas as letras em strings no set sem ordem fixa
print(n_exe)

print('\U0001f315'*40)

# Não repete os elementos ele elimina ótimo para eliminar elementos repetido de uma lista
l1 = [1, 1, 1, 3, 3, 3, 'm', 'm', 'a', 'a', 7, 8, 0]
l1 = set(l1)
l1 = list(l1)
print(l1)

print('\U0001f315'*40)

s1 = {1, 2, 3, 4, 5, 6}
s2 = {1, 2, 3, 7, 8, 9}
s3 = s1 | s2
print(s3)       # Une todos os elementos do set 1 e set 2 que são diferentes entre os dois sets
s4 = s1 & s2
print(s4)       # Une apenas os elementos em comum entre os dois sets.

print('\U0001f315'*40)

s5 = s1 - s2
s5_2 = s2 - s1
print(s5_2)     # Mostra apenas os elementos do primeiro set a esquerda no qual é diferente no caso o s2
print(s5)       # Mostra apenas os elementos do primeiro set a esquerda no qual é diferente no caso o s1

s6 = s1 ^ s2
print(s6)       # Pega os elementos diferentes nos dois sets


