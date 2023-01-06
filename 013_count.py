"""
Count
video 26
https://drive.google.com/drive/folders/1qUALwtScIGRsj62nntvXIrcjlL6lcJYj
"""
from itertools import count

contador = count(start=5, step=2.5)   # Inicia no 5
                                       # Caso queira contagem regressiva so colocar numero negativo
for contagem in contador:
    print(round(contagem, 2))
    if contagem >= 20:
        break

indice = count()
lista = ['marcelo', 'jão', 'andre', 'eliesio']
lista = zip(indice, lista)
print(list(lista))
