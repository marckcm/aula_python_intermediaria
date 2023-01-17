"""
funções decoradoras
decoradores
"""
from time import time
from time import sleep


def fala_oi():
    print('oi')


oi = fala_oi
oi()
print(type(oi))

print('\U0001f500'*20)


def master(funcao):
    def slave(*args, **kwargs):
        print('Função em andamento')
        funcao(*args, **kwargs)
# chama a função dentro da master,
# se não a master vai apenas criar a função.
    return slave


# isso abaixo é um decorador '@master' e acima é uma função decoradora.
# agora toda função que eu criar e colocar esse master ela entra na função decoradora
@master
def entrando():
    print('50%')


@master
def terminada():
    print('Função terminada')


# criada uma função master que executa funções escravas e coloquei
# em uma variável. Chamando a variável ela chama a master que chama
# a escrava que chama a fun_1 que coloca em tela a escrita.
# não e muito usual mais para entender como funciona os decoradores em python
# entrando = master(entrando)

# Aqui chama a variável de entrando não a função entrando se comentar a variável acima ela
# vai chamar a função e não vai aparecer "Função em andamento"
entrando()
terminada()

print('\U0001f500'*20)


def velocidade(funcao):
    def interna(*args, **kwargs):
        inicio = time()
        resultado = funcao(*args, **kwargs)
        fim = time()
        tempo = (fim - inicio) * 1000
        print(f'\nA função {funcao.__name__} levou {tempo:.3f}ms para ser executada.')
        return resultado
    return interna


@velocidade
def demora():
    for i in range(10):
        print(i, end='')
        sleep(1)


# a função decoradora analisa a função demora devido seu decorador '@velocidade'
demora()
