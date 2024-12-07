"""4. **Día 4: Input y Output**
- Función `input()` para recibir datos.
- Función `print()` y formateo de cadenas con f-strings.

Día 4: Input y Output
- **Teoría**:
- Uso de la función `input()` para recibir datos del usuario.
- Formato de salida con `print()`, incluyendo f-strings.

"""

# Las aplicaciones actuales reciben datos del usuario a traves de los dispositivos
# del teclado, o de una pantalla tactil.

# ¿Pero como hacemos que python solicite y reciba esa informacion del usuario?
# Para eso tenemos la funcion INPUT
# Sintaxis

nuevo_nombre =  input("Digite su Nombre: ")
edad = input("Digite su edad")

"""print("el nombre digitado es: " + nuevo_nombre + " y tiene " + edad + " años")"""

# que problema hay? 
# que no podemos concatenar string con enteros. cual es la posible solucion

print("el nombre digitado es: " + nuevo_nombre + " y tiene " + str(edad) + " años")

# pero como podemos ver es algo complicado, se puede enredar
# para esto existen las fstrings, es una forma de formatear cadenas en python
# Sintaxis

print(f"El nombre digitado es: {nuevo_nombre} y tiene {edad} años.")

"""
- **Ejercicio**:
- Escribe un programa que pida al usuario su nombre y edad, y luego imprima un mensaje de saludo.
- **Evaluación**:
- Crea una función que reciba un nombre y devuelva un saludo personalizado
"""

def saludar(nombre, edad):
    print(f"Hola mi nombre es {nombre} y tengo {edad} años")
saludar("Johanna", 41)


