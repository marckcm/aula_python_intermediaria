"""
Tratando exceções em Python
try = tenta executar / funciona como um if (se)
except = exceto caso nao encontre o erro passa para o próximo.
else = quando verifica e seu código passa sem encontra erros
finally = mostra o tipo do erro
"""

try:
    print(a)
except NameError as erro:
    print('Erro de desenvolvimento problema \nsera tratado', erro)

print('-'*40)

try:
    a = []
    print(a[1])
except NameError as erro:
    print('Erro de desenvolvimento problema \nsera tratado', erro)
except IndexError as erro:
    print('Erro de índice')
except Exception as erro:
    print('ocorreu um erro inesperado')
print('-'*40)

try:
    a = {}
    print(a[1])
except NameError as erro:
    print('Erro de desenvolvimento problema \nsera tratado', erro)
except IndexError as erro:
    print('Erro de índice')
except KeyError as erro:
    print('ocorreu um erro de chave')
print('-'*40)


try:
    a = 1
except NameError as erro:
    print('Erro de desenvolvimento problema \nsera tratado', erro)
except IndexError as erro:
    print('Erro de índice')
except Exception as erro:
    print('ocorreu um erro inesperado')
else:
    print("seu código foi executado com sucesso!")

print('-'*40)

try:
    a = 1/0
except NameError as erro:
    print('Erro de desenvolvimento problema \nsera tratado', erro)
except IndexError as erro:
    print('Erro de índice')
except Exception as erro:
    print('ocorreu um erro inesperado')
else:
    pass
finally:
    a = None
print(a)

print('-'*40)
print("mesmo com os erros seu código continua a ser executado")
