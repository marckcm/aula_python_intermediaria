
# Funções - def em Python e return
# cria uma rotina de funções, para que não precise ficar repetindo o código


def funcao(msg):
    print(msg)

funcao("Hello World!")
funcao("Bem Vindo Marcelo")
funcao("tudo bem?")
funcao("Vamos Começar")

funcao("\U0001f320"*20)

def saudacao(msg, nome):
    print(msg, nome)

saudacao("ola", "Marcelo")
saudacao("oi", "Marcelo")
saudacao("Hello", "Marcelo")
saudacao("Bem Vindo", "Marcelo")
saudacao("msg", "nome")

funcao("\U0001f320"*20)

def valores(msg='Olá', nome='usuario'):
    nome = nome.replace('a', '@')           # replace troca as palavras
    msg = msg.replace("o", '0')
    print(msg, nome)
    return f'{msg} {nome}'

valores()           # cria um valor padrao caso nao coloque nada na mensagem
valores(nome="Marcelo")         # altera o nome de usuario para marcelo
valores(nome='marcelo', msg='hi')

funcao("\U0001f320"*20)

texto = valores()
print(texto)

funcao("\U0001f320"*20)

def item(var):
    return var          # assim que a palavra return aparece a função não executa os comandos abaixo

var = item('Valor que eu quero')

if var:
    print(var)
else:
    print('nenhum valor')

funcao("\U0001f320"*20)

def div(n1, n2):
    if n2 == 0:
        return
    return n1/n2

divide = div(7,0)

if divide:
    print(divide)
else:
    print('Conta Invalida')

funcao("\U0001f320"*20)

def f(r1):
    print(r1)

def dumb():
    return f

r1 = dumb()
print(type(r1))
print(id(r1), id(f))            # ID checa o valor da função na memoria significa que é a mesma




