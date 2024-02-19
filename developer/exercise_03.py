"""
Obtener los Elementos Más Frecuentes en una Lista en lenguaje de programación Python.


"""

from collections import Counter

numeros = [1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 5, 6, 5, 5, 6, 7, 8, 9, 9, 9, 8, 9, 9, 9, 10, 10]

contador = Counter(numeros)

print(contador.most_common(8))

palabra = "Python es genial, un lenguaje de programación que abre muchas puertas y ventanas."

print(Counter(palabra).most_common(5))