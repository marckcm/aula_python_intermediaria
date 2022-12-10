# Variavel de escopo global fica fora da 'def' e escopo local dentro de uma função

variavel = 'Sem edição'


def fun():
    print(variavel)


def fun_2():
    global variavel         # altera a variável global mais não uma pratica comum pois em um código grande vc se perde
    variavel = 'editada'
    print(variavel)


def fun_3(arg):
    arg = arg.replace('e', 'au')
    return arg


fun()
fun_2()
print(variavel)

outra_variavel = fun_3(arg=variavel)

print(outra_variavel)

print('\U0001f120'*20)


variavel_2 = 'valor'


def fun_4():
    # print(variavel_2)         # Se simplesmente alterar a variável valor essa função da erro
    # variavel_2 = 'não da certo'
    # print(variavel_2)
    outra_variavel_2 = 'valor 2'      # Jeito certo de se fazer usando o return para retornar a alteração da variável
    return outra_variavel_2


def func_5(arg):
    print(arg)


var = fun_4()           # Coloco a função de alteração de uma variável dentro de outra variável
func_5(var)             # chamo a função que printa na tela o valor da variável alterada
print(variavel_2)       # não altero a variável global.

