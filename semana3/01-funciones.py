"""1. **Día 1: Funciones básicas**
- Definir funciones con `def`.
- Parámetros y valores de retorno."""

# Definicion de Funcion

""" Una función es un bloque de código reutilizable que se ejecuta cuando 
se llama.
"""

def saludar():
    print("Hola Danny")

saludar()


#Parámetros: Puedes pasar valores a una 
# función para personalizar su comportamiento.

def welcome(nombre):
    print(f"Hola {nombre}! ")

welcome("Nana")

#Valores de retorno: Las funciones pueden devolver resultados.

def sumar(a, b):
    return a + b

resultado =  sumar(3,12)

print(resultado)

#Funciones con valores por defecto: Puedes definir valores 
# predeterminados para los parámetros.

def saludar2(nombre="amigo"):
    print(f"Hola {nombre}")
saludar2()
saludar2("Ian")


"""Ejercicio 1: Crear una calculadora básica Escribe una función para sumar, restar, 
multiplicar y dividir dos números.

"""

def calculadora (numero, opcion): #Crea una funcion con parametro llamada calculadora 

    if opcion == "suma":
        print(f"Se imprime la tabla de sumar del {numero}")
        for i in range (1,11):#cada vez que de una vuelta validara cual es la operacion y luego la realizara
            print(f"{numero} + {i} = {numero + i}")
    elif opcion == "resta":
        print(f"Se imprime la tabla de restar  del {numero}")
        for i in range (1,11):
            print(f"{numero} - {i} = {numero - i}")
    elif opcion == "division":
        print(f"Se imprime la tabla de Dividir  del {numero}")
        for i in range(1,11):
            print(f"{numero} / {i} = {numero/i}")
    elif opcion== "multiplicacion":
        print(f"Se imprime la tabla de Multiplicar  del {numero}")
        for i in range(1,11):
            print(f"{numero} * {i} = {numero*i}")
    else: print("No se reconoce ninguna opcion")#si no reconoce ningun comando envia un error y sale del programa

"""opcion = input("Por favor digite la operacion a realizar (suma, resta, multiplicacion, division): ").lower()
try:
    numero = int(input("Escribe el numero a operar: "))
    calculadora(numero, opcion) # invoco la funcion
except ValueError:
    print("Por favor introduce un numero Valido")


"""
while True:
    print("\n=== Menú de la Calculadora ===")
    print("1. Suma")
    print("2. Resta")
    print("3. División")
    print("4. Multiplicación")
    print("5. Salir")

    opcion = input("Elige una opción (1-5): ").strip()
    if opcion == "5":  # Salir del programa
        print("¡Gracias por usar la calculadora! Hasta pronto.")
        break

    # Convertir opción a texto para usar en la función
    opciones_dict = {
        "1": "suma",
        "2": "resta",
        "3": "division",
        "4": "multiplicacion"
    }

    # Validar opción ingresada
    if opcion not in opciones_dict:
        print("Opción no válida, por favor intenta de nuevo.")
        continue

    try:
        numero = int(input("Escribe el número para generar la tabla: "))
        calculadora(numero, opciones_dict[opcion])
    except ValueError:
        print("Por favor, introduce un número válido.")