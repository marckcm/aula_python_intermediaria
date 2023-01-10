"""
Modulo criado em dados tudo que foi executado em dados também é importado
nesse módulo se não for definido no modulo dados com __name__ e __main__
todas as funções e listas em dados podem ser executadas aqui.
"""

import dados

print(dados.PI)
print(dados.multiplica(dados.lista))
for item in dados.pessoas:
    print(item)
print(dados.soma(dados.lista))
