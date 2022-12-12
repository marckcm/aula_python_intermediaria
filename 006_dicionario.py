"""
Dicionário
dict()

"""
import copy

d1 = {'chave': 'valor da chave'}     # O dicionoário vai sempre começar com chaves ter um valor e o explicativo do valor
d1['nova_chave'] = 'significado'    # Adicionando um item na chave
print(d1)

print('\U0001f320'*20)

d2 = {
    'str': 'strings',
    123: 'numeros inteiros',
    (1, 2, 3, 4, 5): 'Tuplas',
}
d2['nomedachave'] = 'agora existe'

print(       d2[1,2,3,4,5]            )
print(d2.get('nomedachave'))            # se não existir a chave no dicionário vai aparecer None

print('\U0001f320'*20)

del d2['str']
print(d2)

print('\U0001f320'*20)

print(len(d2))

print('\U0001f320'*20)

dicionario = {
    'chave_2': 'valor',
    'chave_3': 'Outro Valor',
    'chave_4': 'tupla'
}

for k, v12 in dicionario.items():
    print(k, v12)

print('\U0001f320'*20)

clientes = {
    'cliente1': {
        'nome': 'Marcelo',
        'sobrenome': 'foda',
    },
    'cliente2': {
        'nome': 'Adriana',
        'sobrenome': 'lindona',
    },
    'cliente3': {
        'nome': 'Pedrao',
        'sobrenome': 'bagunceiro',
    },
}

for clientes_k, clientes_v in clientes.items():
    print(f'Exibindo {clientes_k}')
    for dados_k, dados_v in clientes_v.items():
        print(f'\t{dados_k} = {dados_v}')           # /t como se fosse um tab antes do texto cria um espaçamento

print('\U0001f320'*20)

d1 = {1: 'a', 2: 'b', 3: 'c', 4: ['casa', 'apartamento']}

v = d1.copy()           # Cria uma copia do dicionário d1 sendo assim a alteração so é exercida na variável 'v'
v[1] = 'marcelo'
v[4][0] = 'predio'      # nesse caso altera o valor dentro do item 4 a primeira palavra nos dois dicionários
print(d1)
print(v)

# para que não altere o valor do 1 dicionário e preciso importar a função copy do python
print('\U0001f320'*20)

v12 = copy.deepcopy(d1)
v12[4][0] = 'terreno'
v12[4][1] = 'barraco'
print(d1)
print(v12)

print('\U0001f320'*20)

lista = (
    [1, 'a1'],
    [2, 'a2'],
    [3, 'a3'],
)

conv_dicionario = dict(lista)
print(conv_dicionario)
print(conv_dicionario[2])

conv_dicionario.pop(3)          # elimina o item selecionado
print(conv_dicionario)

conv_dicionario.popitem()          # elimina o ultimo item da variavel
print(conv_dicionario)

dicionario2 = {
    'casa': 'quarto',
    'predio': 'sacada',
}
conv_dicionario.update(dicionario2)
print(conv_dicionario)

