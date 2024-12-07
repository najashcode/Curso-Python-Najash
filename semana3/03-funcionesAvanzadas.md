### **Día 3: Funciones Avanzadas**

#### **Teoría:**

1. **Ámbito de las variables (global vs local):**

   En programación, el **ámbito** de una variable determina su accesibilidad dentro de un programa. En Python, hay dos tipos principales de ámbito: **local** y **global**.

   - **Variables locales**: Son aquellas que se definen dentro de una función y solo son accesibles dentro de esa función. Cuando una función termina de ejecutarse, las variables locales dejan de existir.

     Ejemplo de variable local:
     ```python
     def mi_funcion():
         a = 5  # 'a' es local a la función
         print(a)
     mi_funcion()
     # print(a)  # Esto causará un error porque 'a' es local y no está definida fuera de la función
     ```

   - **Variables globales**: Son aquellas que se definen fuera de las funciones, en el cuerpo principal del programa. Las variables globales pueden ser accedidas y modificadas desde cualquier parte del código, incluidas las funciones.

     Ejemplo de variable global:
     ```python
     a = 10  # 'a' es global

     def mi_funcion():
         print(a)  # Accede a la variable global 'a'

     mi_funcion()  # Imprime 10
     ```

     **Importante**: Si deseas modificar una variable global dentro de una función, debes usar la palabra clave `global`.

     Ejemplo de modificación de una variable global:
     ```python
     a = 10  # Variable global

     def mi_funcion():
         global a  # Indica que vamos a modificar la variable global
         a = 20  # Modifica la variable global
     
     mi_funcion()
     print(a)  # Imprime 20
     ```

2. **Funciones lambda:**

   Las **funciones lambda** son funciones anónimas (sin nombre) que se definen en una sola línea y pueden tomar múltiples parámetros, pero sólo pueden contener una expresión. Son útiles cuando necesitas una función simple y no deseas definirla con `def`.

   La sintaxis de una función lambda es:
   ```python
   lambda argumentos: expresión
   ```

   Ejemplo de función lambda:
   ```python
   sumar = lambda x, y: x + y
   print(sumar(3, 4))  # Imprime 7
   ```

   En este ejemplo:
   - `lambda x, y:` define una función anónima que toma dos parámetros, `x` y `y`.
   - `x + y` es la expresión que la función devuelve cuando es llamada.

   Las funciones lambda son muy útiles cuando se necesitan funciones simples y breves, especialmente cuando se pasan como argumentos a otras funciones, como `map()`, `filter()` o `sorted()`.

   Ejemplo de uso con `sorted`:
   ```python
   lista = [(2, 3), (1, 5), (4, 2)]
   lista_ordenada = sorted(lista, key=lambda x: x[1])  # Ordena por el segundo valor de cada tupla
   print(lista_ordenada)  # Imprime [(4, 2), (2, 3), (1, 5)]
   ```

#### **Ejercicio:**

**Crear una función lambda que devuelva el cuadrado de un número:**

La función lambda que devuelve el cuadrado de un número podría definirse de la siguiente manera:

```python
cuadrado = lambda x: x ** 2
print(cuadrado(5))  # Imprime 25
```

Explicación:
- `lambda x:` define una función anónima que toma un parámetro `x`.
- `x ** 2` calcula el cuadrado de `x` (es decir, `x` elevado a la potencia de 2).
- Cuando llamamos a la función `cuadrado(5)`, devuelve 25.

#### **Evaluación:**

**Explica la diferencia entre una función normal y una función lambda:**

1. **Funciones normales:**
   - Se definen usando la palabra clave `def`.
   - Pueden tener varias líneas de código y pueden contener múltiples expresiones, condiciones y bucles.
   - Se utilizan cuando la lógica dentro de la función es más compleja.

   Ejemplo de función normal:
   ```python
   def sumar(x, y):
       return x + y
   ```

2. **Funciones lambda:**
   - Son funciones anónimas, es decir, no tienen nombre.
   - Se definen en una sola línea.
   - Solo pueden contener una expresión, la cual es evaluada y retornada inmediatamente.
   - Se utilizan cuando se necesita una función sencilla y rápida para un propósito específico, generalmente como argumento de otras funciones.

   Ejemplo de función lambda:
   ```python
   sumar = lambda x, y: x + y
   ```

**Resumen de diferencias:**
- Las funciones **normales** son más flexibles, permiten más lógica y se usan para tareas más complejas.
- Las funciones **lambda** son más concisas y se utilizan para operaciones simples, especialmente cuando no es necesario un nombre para la función.

---

Este día de clase te proporciona herramientas adicionales para trabajar con funciones más avanzadas en Python. Entender el **ámbito de las variables** es crucial para gestionar los valores que tu programa usa, y las **funciones lambda** ofrecen una manera eficiente y concisa de crear funciones simples sin la necesidad de definiciones largas.