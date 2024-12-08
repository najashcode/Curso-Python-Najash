### **Día 4: Manejo de Errores (Try/Except)**  

#### **Teoría: Manejo de Excepciones**  
Python permite manejar errores de manera segura utilizando la estructura `try` y `except`. Esto evita que el programa se detenga abruptamente cuando ocurre un error.

#### **Estructura Básica:**
```python
try:
    # Código que podría generar un error
    resultado = 10 / 0
except ZeroDivisionError:
    # Código que se ejecuta si ocurre un error específico
    print("Error: No se puede dividir entre cero.")
```

#### **Cómo Funciona:**
1. **`try`**: Se coloca el código que podría generar un error.
2. **`except`**: Se define el manejo del error específico.
3. **Opcionales**:
   - **`else`**: Se ejecuta si no ocurre ningún error.
   - **`finally`**: Se ejecuta siempre, ocurra o no un error.

---

### **Ejercicio: Manejar Errores al Ingresar un Número**  

#### **Objetivo:**  
Crear un programa que solicite un número y maneje el error si el usuario introduce un valor no numérico.

#### **Código:**
```python
try:
    numero = int(input("Ingresa un número: "))
    print(f"Has ingresado el número {numero}.")
except ValueError:
    print("Error: Debes ingresar un valor numérico.")
```

---

### **Evaluación:**
**¿Qué tipo de error se genera al intentar dividir por cero?**  
- El error que se genera es `ZeroDivisionError`, y ocurre cuando se intenta dividir un número entre cero.

#### **Ejemplo:**
```python
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Error: No puedes dividir entre cero.")
```


# Tipos de Errores

Existen **muchos tipos de errores** (excepciones) que puedes manejar con `try/except` en Python. Aquí te dejo algunos de los más comunes:  

---

### **Errores Comunes en Python:**

1. **`ZeroDivisionError`**: Intentar dividir un número entre cero.  
   ```python
   try:
       resultado = 10 / 0
   except ZeroDivisionError:
       print("Error: División entre cero.")
   ```

2. **`ValueError`**: Ocurre cuando un tipo de dato no es válido.  
   ```python
   try:
       numero = int("Hola")
   except ValueError:
       print("Error: Valor inválido.")
   ```

3. **`TypeError`**: Se genera cuando una operación se realiza entre tipos incompatibles.  
   ```python
   try:
       suma = "Hola" + 5
   except TypeError:
       print("Error: No puedes sumar una cadena y un número.")
   ```

4. **`IndexError`**: Ocurre al intentar acceder a un índice inexistente en una lista.  
   ```python
   try:
       lista = [1, 2, 3]
       print(lista[5])
   except IndexError:
       print("Error: Índice fuera de rango.")
   ```

5. **`KeyError`**: Cuando intentas acceder a una clave inexistente en un diccionario.  
   ```python
   try:
       diccionario = {"nombre": "Danny"}
       print(diccionario["edad"])
   except KeyError:
       print("Error: Clave no encontrada.")
   ```

6. **`FileNotFoundError`**: El archivo especificado no existe.  
   ```python
   try:
       archivo = open("archivo_inexistente.txt", "r")
   except FileNotFoundError:
       print("Error: Archivo no encontrado.")
   ```

7. **`ImportError`**: Cuando un módulo no puede importarse.  
   ```python
   try:
       import modulo_inexistente
   except ImportError:
       print("Error: No se puede importar el módulo.")
   ```

8. **`AttributeError`**: Acceder a un atributo que no existe.  
   ```python
   try:
       cadena = "Hola"
       cadena.append("!")
   except AttributeError:
       print("Error: El objeto 'str' no tiene ese atributo.")
   ```

---

### **Captura de Errores Genéricos:**
Si no estás seguro del tipo de error, puedes usar una excepción genérica:  
```python
try:
    resultado = 10 / "cinco"
except Exception as e:
    print(f"Ocurrió un error: {e}")
```

---

### **Combinar Excepciones Específicas:**
```python
try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    numero = int(contenido)
except (FileNotFoundError, ValueError) as e:
    print(f"Error: {e}")
```

---

### **Conclusión:**  
Manejar excepciones te permite crear programas más robustos y evitar que se detengan inesperadamente. ¿Te gustaría profundizar en alguno de estos errores? 🚀


# Ejercicios
Aquí tienes algunos ejercicios que combinan funciones, funciones lambda y manejo de errores:

### Ejercicio 1: Función que calcula el cuadrado de un número con manejo de error
1. Crea una función que reciba un número y calcule su cuadrado.
2. Utiliza una función `lambda` para calcular el cuadrado de un número.
3. Añade manejo de errores para verificar si el valor ingresado es un número válido. Si no lo es, muestra un mensaje de error.

**Pistas:**
- La función debe devolver el cuadrado de un número.
- Utiliza `try` y `except` para capturar errores si el valor no es un número.

### Ejercicio 2: Función que calcula el área de un triángulo con parámetros por defecto
1. Crea una función que calcule el área de un triángulo. La fórmula es: \( \text{Área} = \frac{base \times altura}{2} \).
2. Usa un valor por defecto para la altura (por ejemplo, 10) y permite que el usuario ingrese la base.
3. Añade manejo de errores para asegurarte de que el valor de la base es un número positivo. Si no lo es, muestra un mensaje de error.

**Pistas:**
- Si el valor de la base es negativo o no es un número, el programa debe capturar el error y mostrar un mensaje adecuado.

### Ejercicio 3: Función que calcula la raíz cuadrada de un número
1. Crea una función que calcule la raíz cuadrada de un número.
2. Usa una función `lambda` para calcular la raíz cuadrada de un número.
3. Añade manejo de errores para manejar los siguientes casos:
   - Si el número ingresado no es positivo.
   - Si el valor ingresado no es un número.

### Ejercicio 4: Calculadora simple con manejo de errores
1. Crea una función que realice las operaciones básicas de suma, resta, multiplicación y división.
2. La función debe aceptar dos números y una operación.
3. Añade un manejo de errores para:
   - Asegurarte de que los números son válidos.
   - Evitar la división por cero.
   - Asegurarte de que la operación es una de las permitidas (suma, resta, multiplicación, división).

### Ejercicio 5: Filtrar números positivos
1. Crea una lista de números que contiene algunos valores negativos y algunos no numéricos (como cadenas de texto).
2. Usa una función `lambda` para filtrar y obtener solo los números positivos.
3. Utiliza manejo de errores para asegurarte de que no se incluyen valores no numéricos en la lista de resultados.

---

### Tip:
Para cada ejercicio, asegúrate de que el código esté lo más organizado posible y realiza pruebas con diferentes tipos de entradas para verificar que el manejo de errores funcione correctamente. ¡Avísame cuando hayas terminado alguno para revisarlo! 😊