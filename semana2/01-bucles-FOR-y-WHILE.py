
print(" --------------- Ciclo For ------------------")
# El ciclo for se utiliza cuando sabes cuántas veces quieres que se repita un bloque de código. 
# Es ideal para iterar sobre secuencias como listas, cadenas de texto o rangos numéricos.

#Sintaxys

#for variable in iterable:
    # Código que se ejecuta en cada iteración


"""Aquí:

variable: Es la que toma cada valor del iterable en cada iteración.
iterable: Puede ser una lista, una cadena de texto, un rango, etc."""
print("--- For en Listas ---")
frutas = ["manzana", "banana", "cereza"]
for fruta in frutas:
    print(fruta)

# Ejemplo 2: Usar range() para iterar sobre un rango de números:
print("---For con Range ---")
for i in range(5):
    print(i)


"""Modificando el range():
Si quieres que el rango comience desde un número diferente 
o se incremente por otro valor que no sea 1, puedes especificar 
el inicio, el fin y el paso:"""
print("--- modificando el Range ---")
for i in range(2, 10, 2):
    print(i)

#Esto imprimirá los números entre 2 y 10 (sin incluir el 10) y en pasos de 2.

# Ejemplo 3: Iterar sobre una cadena de texto:
print("---Iterar en cadenas de texto ---")
for letra in "Python":
    print(letra)


# -----------------Bucle WHile-------------
print("---------- Bucle WHILE -------------")

"""El ciclo while se usa cuando no sabes exactamente
 cuántas veces se repetirá el ciclo, 
 pero quieres que continúe hasta que una condición deje de ser verdadera.

"""
# Sintaxis del ciclo while:
""" while condición:
    # Código que se ejecuta mientras la condición 
    # sea verdadera

condición: Es una expresión que se evalúa como 
verdadera o falsa. Mientras sea verdadera, el 
bloque de código se seguirá ejecutando.

"""
#Ejemplo 1: Usar while con una condición simple:

contador = 0
while contador < 5:
    print(contador)
    contador += 1  # Incrementa el contador en 1 en cada iteración

#Ejemplo 2: Ciclo que espera una entrada del usuario:

respuesta = ""
while respuesta != "si":
    respuesta = input("¿Quieres salir? ")

# Ejercicios para practicar
# Ciclo for: Imprime los números del 1 al 10.

for num in range(1,11):
    print (num)

# Ciclo while: Crea un ciclo que imprima los números del 1 al 10, pero usando while.

numero = 0
while numero <= 10:
    print (numero)
    numero += 1


