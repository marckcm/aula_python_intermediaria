"""
erros
"""


def converter(digito):
    try:
        digito = int(digito)
        return digito
    except ValueError:
        try:
            digito = float(digito)
            return digito
        except ValueError:
            pass


numero = converter(input("Digite um numero: "))
if numero is None:
    print("Isso não é um numero")
else:
    print(numero * 5)

