"""**Día 2: Listas**
- Creación, modificación y acceso a listas.
- Iterar sobre listas con bucles.

Día 2: Listas
- **Teoría**:
- Creación, modificación y acceso a elementos de listas.
- Métodos comunes: `append()`, `remove()`, `pop()`, `len()`.
- **Ejercicio**:
- Crea una lista de tus frutas favoritas y muestra la primera y última fruta.
- **Evaluación**:
- ¿Qué sucede si intentas acceder a un índice fuera del rango de la lista?"""

"""
¿Qué es una lista?
Una lista es una colección ordenada y mutable de elementos. 
Los elementos en una lista pueden ser de diferentes tipos (números, cadenas, booleanos, incluso otras listas),
 y se almacenan en un orden secuencial. Además, las listas pueden cambiarse (son mutables), 
 lo que significa que puedes agregar, eliminar o modificar elementos después de crearla
"""
# Sintaxys de una lista
# nombre_lista =[elemento1, elemento2, elemento3]

# Las listas se definen por medio de los corchetes, es decir, los elementos
# se encierran dentro de corchetes para generar una lista.

numeros = [1, 2, 3, 4, 5]
persona = ["nombre", "edad", "Telefono"]
mi_lista = [28, "Python", True, 3.14]

"""Acceso a los elementos de una lista
Puedes acceder a los elementos de una lista utilizando índices, que comienzan desde 0 
(el primer elemento tiene índice 0, el segundo tiene índice 1, y así sucesivamente)."""

frutas = ["manzana", "fresa", "Limon", "cereza"]
print(frutas[0])
print(frutas[3])
print(frutas[-1])
print(frutas[-3])
print(frutas)

"""
**** Modificar elementos de una lista ****
Ya que las listas son mutables, 
puedes cambiar el valor de cualquier 
elemento accediendo a su índice.
"""

frutas[1] = "naranja"  # Cambia "banana" por "naranja"
print(frutas)

""" *** Agregar elementos a una lista ***
Existen varias formas de añadir nuevos
 elementos a una lista:
"""

# Usando el metodo Append("elemento a añadir"):, que añade un elemento
# al final de la lista

frutas.append("Maracuya")
print(frutas)

# Usando el metodo  insert(el indice, "elemento"):
# Inserta un elemento en una posición específica.

frutas.insert(0, "Melocoton")
print(frutas)

# Eliminar elementos de una lista
# Tambien hay varias formas de eliminar los elementos
# de una lista

# Usando el metodo remove("elemento"): 
# Elimina la primera aparición de un valor específico.

frutas.remove("manzana")
print(frutas)

frutas.remove("naranja")
frutas.remove("cereza")
print(frutas)

frutas.append("Manzana")
frutas.append("Fresa")
frutas.append("Cereza")
print(frutas)

#Usando el metodo pop(): 
# Elimina y devuelve el elemento en un índice específico (por defecto, el último).

frutas.pop(2)
print(frutas)

frutas.pop()
print(frutas)

# Usando el metodo del: 
# Elimina el elemento en un índice dado o incluso la lista completa.

del frutas[2]
print (frutas)

del frutas[1]
print (frutas)

# Usando el Metodo clear(): 
# Elimina todos los elementos de la lista, 
# dejando la lista vacía.

frutas.clear()
print(frutas)

print("****************************")
"""
Longitud de una lista
Puedes obtener la cantidad de 
elementos en una lista usando la función len().
"""

numeros = [1,2,213,4,5,6,23]
print(len(numeros))

print("****************************")
"""Slicing (rebanado) de listas
El slicing te permite obtener una parte (sublista) 
de una lista, utilizando la siguiente sintaxis:

"""
# sublista = lista[inicio:fin]
division = numeros[0:4]
print (division)

print("*****Tema 2: Iteracion con listas*******")
#El ciclo for es muy útil para iterar 
# sobre los elementos de una lista.

colores = ["Rojo", "Verde", "Naranja"]
print("Comenzando Verificacion")
for color in colores:
    if color == "Amarillo":
        print("Verificando: Amarillo Detectado")
    else: print("Verificando: No pasó")

print("***** Otras operaciones *********")
# Comprobar si un elemento está en la lista:
# Usando in puedes verificar si un elemento 
# está presente.

print ("Amarillo" in colores)


print("Comenzando Verificacion")
for verified in colores:
    if ("Amarillo" in colores):
        print("Verificando: Amarillo Detectado")
        break
    else: print("Verificando: No pasó")