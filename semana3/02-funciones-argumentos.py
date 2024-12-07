"""Día 2: Funciones con argumentos

- **Teoría**:
- Funciones con varios parámetros y argumentos por defecto.

- **Ejercicio**:
- Crea una función que calcule el área de un rectángulo. Permite un parámetro por defecto para la altura.

- **Evaluación**:
- ¿Qué sucede si no se pasan argumentos a una función que los requiere?"""

def suma(a,b):
    return a+b


def saludar(nombre="juan"):
    print(f"Hola {nombre}")

saludar("Danny")


#### **Ejercicio:**
#**Crear una función que calcule el área de un rectángulo, con un parámetro por defecto para la altura.**

#Area = base X altura

def area(base, altura=3): #definir funcion area con parametros base y altura donde altura tiene un valor predeterminado de 3

    calculo = base * altura # creo una variable calculo que almacena la operacion solicitada base X altura
    return calculo #devuelvo el valor de calculo

resultado = area(2, 4) #Creo una variable resultado para guardar la invocacion de la funcion
print(f"El area del rectangulo es {resultado}") #imprimo 

