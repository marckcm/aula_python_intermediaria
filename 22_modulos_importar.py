"""
modulos
São arquivos externos que você pode importar para o seu sistema python
para expandir as funcionalidades da linguagem python
https://docs.python.org/3/py-modindex.html
"""

# Para importar a biblioteca de SYS
import sys
# Para importar apenas um comando especifico da biblioteca.
from sys import platform
# Para mudar o nome do comando ou da biblioteca na hora de chamar o comando ficar mais fácil
from sys import platform as so
import random


print(sys.platform)
print(platform)
print(so)

print("\U0001f502"*20)

for num in range(10):
    print(random.randint(0, 10))
