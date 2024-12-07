"""Ejercicio
1 Crea una tupla llamada colores que contenga los valores "rojo", "verde" y "azul".
2 Imprime el segundo elemento de la tupla.
3 Crea una nueva tupla llamada colores_extras con los valores "amarillo" y "violeta", y concaténala con la tupla colores para crear una tupla completa llamada todos_los_colores.
4 Desempaqueta todos_los_colores en variables individuales e imprime cada color en una línea separada.
5 Prueba los ejercicios y cuéntame si tienes dudas o quieres que revise tus respuestas. ¡Adelante!

"""

colores = ("rojo", "verde", "azul")
print(colores[1])

colores_extras=("amarillo", "Violeta")
todos_losColores = colores + colores_extras
print(todos_losColores)
rojo, verde, azul, amarillo, violeta = todos_losColores
print(rojo)
print(verde)
print(azul)
print(amarillo)
print(violeta)