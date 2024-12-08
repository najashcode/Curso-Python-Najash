"""Día 3: Funciones avanzadas
- **Teoría**:
- Ámbito de las variables (global vs local).
- Funciones lambda.
- **Ejercicio**:
- Crea una función lambda que devuelva el cuadrado de un número.
- **Evaluación**:
- Explica la diferencia entre una función normal y una función lambda."""

# Variables Locales
def local():
    a=1
    print(a)
local()

#Variables Globales

b = 4

def variable_global():
    print(b)
variable_global()


#Modificar variables globales dentro de funciones

e = 12
print(e)
def mi_funcion():
    global e
    e = 32

mi_funcion()
print(e)

#Funciones LAMBDA

sumar = lambda x,y: x+y
print(sumar(3,4))

# es lo mismo que hacer esto

"""def sumar(x,y):
    operacion = x + y
    print (operacion)
sumar(3,4)"""

lista = [(2, 3), (1, 5), (4, 2)]
lista_ordenada = sorted(lista, key=lambda x: x[1])  # Ordena por el segundo valor de cada tupla
print(lista_ordenada)  # Imprime [(4, 2), (2, 3), (1, 5)]

cuadrado = lambda x: x**2
print(cuadrado(4))

"""Una funcion normal, es definida por la palabra reservada DEF
a esta se le puede o no ingresar parametros, mientras que la 
funcion lambda no es definida y se le pasa los parametros
en la misma linea, se conoce como funciones anonimas"""

