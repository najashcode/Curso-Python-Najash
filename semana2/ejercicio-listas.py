# Crea una lista de tus frutas favoritas y muestra la primera y última fruta.

frutas = ["Kiwi", "Mandarina", "Sandia", "Melon", "Banano"]
print(frutas[0])
print(frutas[4])

"""Ejercicio
1. Crea una lista llamada numeros que contenga los números del 1 al 10.
2. Imprime el tercer elemento de la lista.
3. Cambia el último valor de la lista por el número 20.
4. Elimina el primer elemento de la lista.
5. Usa un ciclo for para imprimir cada elemento de la lista"""

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numeros[3])

numeros[9] = 20
print (numeros)

numeros.remove(1)
print(numeros)

for numero in numeros:
    print(numero)