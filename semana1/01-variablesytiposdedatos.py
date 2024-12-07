"""
Día 2: Variables y tipos de datos
- **Teoría**:
- Tipos de datos: enteros, flotantes, cadenas, booleanos.
- Asignación de variables y convenciones de nombres.
- Conversión de tipos: `int()`, `float()`, `str()`.

"""

"""
En python tenemos diferentes tipos de datos. Los mas usados son:
enteros, flotantes, cadenas, booleanos.
Los tipos de datos también se utilizan para determinar cómo se almacenan los 
valores en la memoria de la computadora y cómo se pueden manipular y 
operar los valores. Por ejemplo, los números enteros se almacenan como 
secuencias de bits en la memoria, y se pueden realizar operaciones 
aritméticas como suma, resta, multiplicación y división.

"""
#Tipos de Datos enteros
# Son normalmente numeros enteros

x = 24
print (type(x)) # la funcion type me muestra en pantalla el tipo de dato que estoy utilizando
print(x)

# Al asignar el valor 24 a la variable x python de manera automatica reconoce
# un entero.

# Tipos de datos FLoat
# ¿pero que pasa si el dato es un decimal o si el resultado de una operacion
# devuelve un decimal?

PI = 3.14
print(PI)
print(type(PI))

# Python reconoce un nuevo tipo de dato, ahora es un FLOAT o flotante.

# Tipos de datos String

# Todo texto o cadena de texto es reconocido como un STRING  o STR

nombre = "Danny"
print (nombre)
print(type(nombre))

"""
las cadenas de texto o Str deben ir siempre entre comillas ya sean simples o dobles
"""

# Tipos de datos booleanos

# son datos de si o no Verdadero o falso true False se utilizan para condicionar algoritmos

x= True
y=False
print(x, y)
print(type(x))

a=3
b=4.5
suma = a+b
print(suma)
print(type(suma))

#Cambiemos el tipo a una variable
print("Cambio de tipo de variable")
variable1 = 4.5 #float
variable2 = 35 #int
variable3 = "Hola Mundo" #str
print (type(variable1))
print(type(variable2))
print(type(variable3))

variableCambio = str(variable2)
print(variable3 + variableCambio)
#print(variable3 + str(variable2))
print(int(variable1))
print(float(variable2))

"""
Aqui termina esta clase

a continuacion tareas y evaluaciones

- **Ejercicio**:
- Crea un programa que declare variables de diferentes tipos y muestre sus valores y tipos.
- **Evaluación**:
- ¿Qué tipo de dato es el resultado de la expresión `3 + 4.5`?


"""