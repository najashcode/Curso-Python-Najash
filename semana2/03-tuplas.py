# - Diferencias entre listas y tuplas.
#- Operaciones con conjuntos.

"""Día 3: Tuplas y conjuntos
- **Teoría**:
- Definición y características de tuplas y conjuntos.
- Operaciones básicas con tuplas y conjuntos.
- **Ejercicio**:
- Crea una tupla con los días de la semana y un conjunto con algunos números.
- **Evaluación**:
- Explica la diferencia entre listas y tuplas."""

""" Comencemos 

¿Qué es una tupla?

Una tupla es una estructura de datos en Python
similar a una lista, ya que puede almacenar 
múltiples valores. 
Sin embargo, la diferencia principal es 
que las tuplas son inmutables, es decir, 
una vez que creas una tupla, no puedes cambiar,
agregar ni eliminar elementos de ella.

Sintaxis de una tupla:

Las tuplas se definen con paréntesis () 
y los elementos se separan por comas.

mi_tupla = (elemento1, elemento2, elemento3)

"""
coordenadas = (10, 20)
# Nota: Aunque las tuplas se definen comúnmente con paréntesis, también puedes crearlas sin ellos:

otra_tupla = 1, 2, 3

"""Acceso a los elementos de una tupla
Al igual que en las listas, puedes acceder a los elementos de una tupla usando índices. 
Estos índices comienzan en 0.

"""
mi_tupla = ("rojo", "verde", "azul")
print(mi_tupla[0])  # Accede al primer elemento
print(mi_tupla[2])  # Accede al tercer elemento
print(mi_tupla[-1])  # Accede al último elemento

"""¿Por qué usar tuplas en lugar de listas?
Inmutabilidad: Como las tuplas no se pueden modificar después de ser creadas, son más seguras si necesitas una estructura de datos que no deba cambiar. Esto las hace ideales para almacenar datos constantes.

Eficiencia: Las tuplas ocupan menos espacio en memoria y se procesan más rápidamente que las listas, lo cual puede ser útil en ciertas aplicaciones.

Desempeño en Diccionarios y Conjuntos: Las tuplas pueden ser usadas como claves en diccionarios (ya que son inmutables), mientras que las listas no."""

"""Operaciones con tuplas
Aunque no puedes modificar las tuplas 
directamente, hay varias operaciones 
útiles que puedes realizar con ellas:

Concatenar tuplas: Puedes unir dos tuplas 
con el operador +."""

tupla1 = (1, 2, 3)
tupla2 = (4, 5)
nueva_tupla = tupla1 + tupla2
print(nueva_tupla)

#Repetir una tupla: Puedes repetir una tupla usando el operador *.

mi_tupla = ("hola",) * 3
print(mi_tupla)

"""Comprobar si un elemento está en la tupla: 
Usando in, puedes verificar si un elemento 
está presente en la tupla.

"""

print(10 in coordenadas)

"""Longitud de una tupla: 
Para obtener la cantidad de elementos en 
una tupla, usa len().

"""
print(len(mi_tupla))

print("Desempaquetado de tuplas")
"""Una característica útil de las tuplas 
es que puedes desempaquetarlas asignando 
sus valores directamente a varias variables. 
Esto es especialmente útil en funciones 
que devuelven múltiples valores.

"""
punto = (4, 5)
x, y = punto  # Desempaqueta la tupla en dos variables
print(x)
print(y)

colores = ("amarillo", "azul", "rojo")
c1,c2,c3 = colores
print(c1)
print(c2)
print(c3)

print("Tuplas y funciones")
"""Las tuplas son comunes en funciones 
que necesitan devolver múltiples valores, 
ya que permiten agrupar
los valores de retorno.

"""
def dividir(a, b):
    cociente = a // b
    residuo = a % b
    return cociente, residuo

resultado = dividir(10, 3)
print(resultado)

"""Comparación entre listas y tuplas
Característica	Listas	Tuplas
Mutabilidad	Mutable (pueden cambiarse)	Inmutable (no cambian)
Sintaxis	[ ]	( )
Uso en diccionarios	No se puede usar como clave	Se puede usar como clave
Tamaño en memoria	Ocupa más espacio	Ocupa menos espacio
"""