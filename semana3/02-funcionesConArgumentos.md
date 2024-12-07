Claro, te explico detalladamente la clase de mañana que estás planeando.

### **Día 3: Funciones con retorno de valores**

#### **Teoría:**

- **Funciones con retorno de valores:**
  En Python, las funciones pueden devolver valores utilizando la palabra clave `return`. El valor que devuelve una función puede ser un cálculo, una variable, una cadena de texto o cualquier tipo de dato. El `return` permite que la función entregue un resultado que pueda ser utilizado en otras partes del programa.

  La sintaxis básica de una función con retorno es la siguiente:

  ```python
  def nombre_funcion(parametros):
      # Realizar alguna operación
      return resultado
  ```

  Ejemplo simple:

  ```python
  def suma(a, b):
      return a + b

  resultado = suma(3, 4)  # Aquí se guarda el valor retornado
  print(resultado)  # Imprime 7
  ```

  En este caso, la función `suma` recibe dos parámetros (`a` y `b`), realiza la suma de ambos y retorna el resultado. Este valor se puede almacenar en una variable o utilizar directamente.

- **¿Qué significa `return`?**
  La palabra clave `return` se utiliza para salir de una función y enviar un valor de vuelta al lugar donde fue llamada. Después de ejecutar un `return`, el control de ejecución se transfiere fuera de la función, y cualquier código posterior al `return` dentro de la función no se ejecutará.

  Ejemplo:
  ```python
  def saludo():
      print("Hola!")
      return "Adiós"

  print(saludo())  # Imprime "Hola!" y luego "Adiós"
  ```

  En este caso, la función imprime "Hola!" y luego retorna "Adiós". El valor "Adiós" es el valor que se obtiene cuando se llama a la función.

#### **Ejercicio:**

**Crear una función que calcule el área de un triángulo y retorne el resultado.**

La fórmula para el área de un triángulo es:

\[
\text{Área} = \frac{base \times altura}{2}
\]

Por lo tanto, puedes crear una función que reciba dos parámetros: la base y la altura del triángulo, y retorne el área calculada.

Ejemplo de código:

```python
def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    return area
```

En este caso:

- **Parámetros**: `base` y `altura` son los parámetros que la función acepta.
- **Cálculo**: La fórmula `(base * altura) / 2` calcula el área del triángulo.
- **Retorno**: La función `return area` devuelve el valor calculado.

Ejemplo de uso de la función:

```python
resultado = calcular_area_triangulo(5, 10)
print(f"El área del triángulo es: {resultado}")
```

Esto imprimirá el resultado del cálculo del área.

#### **Evaluación:**

- **¿Por qué usar `return` en lugar de simplemente imprimir los resultados?**
  Usar `return` permite que la función sea más flexible. El valor que se retorna puede ser utilizado en otras partes del código o guardado en una variable. Esto hace que la función sea más reutilizable y facilita la composición de funciones más complejas.

  Ejemplo:

  ```python
  def cuadrado(x):
      return x * x
  
  def suma_cuadrados(a, b):
      return cuadrado(a) + cuadrado(b)

  resultado = suma_cuadrados(3, 4)
  print(resultado)  # Imprime 25 (9 + 16)
  ```

  Aquí, hemos utilizado el `return` para crear una función `suma_cuadrados` que utiliza el resultado de otras funciones, demostrando cómo se puede reutilizar el valor retornado.

- **¿Qué sucede si no hay un `return` en una función?**
  Si una función no tiene un `return`, entonces la función no devolverá ningún valor. Esto es útil si no necesitas un resultado específico de la función, pero aún así quieres realizar alguna operación o acción.

  Ejemplo:

  ```python
  def saludo():
      print("Hola!")
  
  resultado = saludo()
  print(resultado)  # Imprime "Hola!" y luego "None"
  ```

  En este caso, la función `saludo` no tiene `return`, por lo que su valor de retorno es `None`. Esto significa que cuando se guarda en la variable `resultado`, su valor es `None`.

#### **Resumen:**

1. **`return` devuelve un valor:** Se usa para salir de la función y devolver un valor que puede ser utilizado más adelante en el código.
2. **Las funciones con `return` son más reutilizables:** Puedes almacenar el resultado de una función y usarlo en cualquier parte del programa.
3. **Cuando no hay `return`, la función no devuelve nada:** El valor por defecto que devuelve una función sin `return` es `None`.

---

Esta clase te ayudará a comprender cómo utilizar `return` para devolver valores y hacer que tus funciones sean más flexibles, permitiendo que los resultados se puedan almacenar o usar en otras partes de tu programa.