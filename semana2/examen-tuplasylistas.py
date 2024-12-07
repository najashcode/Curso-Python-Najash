print("Parcial Tuplas y Listas")

"""Lista: Crea una lista de 10 números enteros 
y realiza las siguientes operaciones:
Imprime el primer y el último elemento. ok
Cambia el valor del quinto elemento a 100. ok
Agrega un nuevo número al final de la lista.ok
Ordena la lista en orden ascendente.ok

"""

numeros_enteros = [1, 2, 5, 4, 3, 6, 7, 8, 9, 10]
print(numeros_enteros[0])
print(numeros_enteros[9])
print(numeros_enteros)
numeros_enteros[4] = 100
print(numeros_enteros)

numeros_enteros.append(28)
print(numeros_enteros)

numeros_enteros.sort()
print(numeros_enteros)

"""Tupla: Crea una tupla de 5 elementos con nombres de 
ciudades. OK
 Intenta modificar el segundo elemento y observa 
el error que ocurre. Luego, convierte la tupla en una lista, 
realiza la modificación y vuelve a convertirla en una tupla.

"""

ciudades = ("Bogotá", "Barranquilla", "Medellín", "Santa Marta")
print(ciudades)
lista_de_tupla = list(ciudades)
print(lista_de_tupla)
lista_de_tupla[2] = "Cartagena"
print(lista_de_tupla)

"""2. Operaciones con Listas y Tuplas
Intersección y Unión:
Crea dos listas de números, list1 y list2, 
cada una con 5 elementos. Encuentra los elementos que 
están en ambas listas (intersección) y los que están en 
al menos una de ellas (unión).
Convierte ambas listas en tuplas y repite el ejercicio, 
imprimiendo los resultados.
"""

list1 = [1, 21, 43, 66, 74]
list2 = [18, 56, 66, 98, 95]
print(list1)
print(list2)

interseccion = list(set(list1) & set(list2))
print (interseccion)
# es mas facil con set

union = list(set(list1) | set(list2))
print (union)
union.sort()
print(union)

tupla_list1 = tuple(list1)
tupla_list2 = tuple(list2)
print(tupla_list1)
print(tupla_list2)

interseccion_tupla = tuple(set(tupla_list1) & set(tupla_list2))
print (interseccion_tupla)

union_tupla = tuple(set(tupla_list1) | set(tupla_list2))
print(union_tupla)
tuplas_ordenadas = sorted(union_tupla)
print(tuplas_ordenadas)