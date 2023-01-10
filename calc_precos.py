

def real(valor):
    return f'R$ {valor:.2f}'.replace(".", ",")


def aumento(valor, porcentagem, formata=False):
    r = valor + (valor * (porcentagem / 100))

    if formata:
        return real(r)
    else:
        return r


def reducao(valor, porcentagem, formata=False):
    n = valor - (valor * (porcentagem / 100))

    if formata:
        return real(n)
    else:
        return n





