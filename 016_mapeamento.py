from dados import produtos, pessoas, lista

'''
Mapeamento
map = mapeamento de dados
dentro de um dicionario pode ser pego apenas a coluna solicitada e colocar ela em uma lista.
'''

def aumento(p):
    p['preco'] = round(p['preco'] * 1.05, 2)    #round coloca casas decimais
    return p


alterar_valor = map(aumento, produtos)

for item in alterar_valor:
    print(item)

print('\U0001f500'*20)

nomes = map(lambda p: p['nome'], pessoas)


for linha in nomes:
    print(linha)
