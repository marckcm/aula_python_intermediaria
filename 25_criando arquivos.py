"""
https://docs.python.org/3/library/functions.html#open
criando lendo escrevendo e apagando arquivos
'open' cria o arquivo
'w+' cria arquivo texto
'r' le o arquivo ja criado
'a+' um arquivo ja criado ele adiciona coisas
"""

# 3 modo e mais utilizado em python
# esse modo não precisa mandar fechar o arquivo assim que acabar ele fecha
with open('intro.txt', 'w+') as file:
    file.write('linha 1\n')
    file.write('linha 2\n')
    file.write('linha 3\n')
    file.write('linha 4\n')
    file.seek(0, 0)
    print(file.read())

with open('intro.txt', 'r') as file:
    print(file.read())

with open('intro.txt', 'a+') as file:
    file.write(f'continuação com o texto adicionado\n')
    file.seek(0, 0)
    print(file.read())


# 2 modo de criação so tirar o comentário com o ctrl + /

# try:
#     file = open('intro.txt', 'w+')
#     file.write('linha 1\n')
#     file.write('linha 2\n')
#     file.write('linha 3\n')
#     file.write('linha 4\n')
#     file.seek(0, 0)
#     print(file.read())
# finally:
#     file.close()


# 1 modo de criação so tirar o comentário com o ctrl + /

# file = open('intro.txt', 'w+')
# file.seek(0, 0)
# print('Lendo Documento')
# print(file.read(), end='')
#
# print('\U0001f520'*40)
#
# file.seek(0, 0)
# # readlineLê linha por linha e o end para não dar a quebra de linha
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
# print(file.readline(), end='')
#
# print('\U0001f520'*40)
#
# file.seek(0, 0)
# for linha in file.readlines():
#     print(linha, end='')
# file.close()

