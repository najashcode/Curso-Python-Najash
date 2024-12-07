"""4. **Día 4: Diccionarios**
- Crear y modificar diccionarios.
- Acceder a valores por claves.

Día 4: Diccionarios
- **Teoría**:
Que es un Diccionario
Un diccionario en Python es una colección desordenada, modificable 
e indexada de elementos, donde cada elemento es un par de clave y valor.
Se define con llaves {} y cada par de clave-valor se separa por una coma.
ejemplo
"""
estudiante = {
    "nombre": "Danny",
    "apellido": "Kent",
    "edad": 25,
    "curso": "Python",
    "notas": [90, 85,98]
}
"""
- Acceso a valores por claves.
Puedes acceder a un valor usando su clave en el diccionario.
"""
print(f"El nombre del estudiante solicitado es {estudiante["nombre"]} {estudiante["apellido"]}")

"""Agregar o Modificar Elementos

Puedes añadir un nuevo par clave-valor o 
modificar uno existente.
"""
estudiante["promedio"] = 85
print (estudiante)

"""
Eliminar elementos
Puedes eliminar pares clave-valor con el método pop() o con del.

"""
estudiante.pop("curso")
print(estudiante)

estudiante["Curso"] = "Python"
print(estudiante)

# Otra forma de eliminar es con el metodo DEL

del estudiante["notas"]
print(estudiante)

print("****** Recorrer un Diccionario********")
"""

Puedes recorrer el diccionario para ver todas sus 
claves y valores.

"""
for clave, valor in estudiante.items():
    print(clave, ":", valor)

"""
Metodos Utiles en diccionarios
keys(): Devuelve una lista con todas las claves.
values(): Devuelve una lista con todos los valores.
items(): Devuelve pares clave-valor en forma de tuplas.
clear(): Vacía el diccionario"""

"""

- **Ejercicio**:
Crea un diccionario llamado libro con la siguiente 
información:
Título: "El Principito"
Autor: "Antoine de Saint-Exupéry"
Año: 1943
Género: "Ficción"

- **Evaluación**:
- ¿Qué método usarías 
para obtener todas las claves de un diccionario?
Usaria el metodo keys
"""

libros = { # Se crea el diccionario libros
    "titulo": "El Principito",
    "Autor": "Antoine de Saint-Exupéry",
    "Año": 1943,
    "Género": "Ficción"
}

print(libros["Año"]) # Imprime la clave año

libros["Idioma"] = "Frances" # Añado una clave idioma con el valor frances
print(libros)

libros["Año"] = 1944 # Modifico el año
print (libros)

libros.pop("Género") # Elimino la clave genero
print(libros)

for clave, valor in libros.items():
    print(clave, ":", valor)

