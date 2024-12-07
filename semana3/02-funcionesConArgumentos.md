### **Día 2: Funciones con Argumentos**

#### **Teoría:**
- **Funciones con varios parámetros:**  
  Las funciones en Python pueden aceptar varios parámetros. Los parámetros son variables que la función usa para realizar operaciones. Cuando defines una función, puedes especificar múltiples parámetros separados por comas.

  Ejemplo:
  ```python
  def suma(a, b):
      return a + b
  ```

  En este caso, la función `suma` acepta dos parámetros: `a` y `b`.

- **Argumentos por defecto:**  
  A veces, puedes querer que una función acepte un parámetro que tenga un valor predeterminado si no se pasa un valor al llamarla. Para hacerlo, simplemente asignas un valor al parámetro dentro de la definición de la función.

  Ejemplo:
  ```python
  def saludar(nombre="Juan"):
      print(f"Hola, {nombre}!")
  ```

  Aquí, si no se pasa un argumento cuando llamas a `saludar()`, se usará "Juan" como valor predeterminado. Esto es útil si deseas proporcionar una opción predeterminada sin que sea obligatorio que el usuario la ingrese.

#### **Ejercicio:**
**Crear una función que calcule el área de un rectángulo, con un parámetro por defecto para la altura.**

Para este ejercicio, vamos a crear una función que calcule el área de un rectángulo. Recordemos que la fórmula para calcular el área de un rectángulo es:

\[ \text{Área} = \text{base} \times \text{altura} \]

Queremos que la función reciba dos parámetros: la base y la altura. Sin embargo, si no se pasa la altura, debe tener un valor predeterminado.

Aquí tienes un ejemplo:

```python
def calcular_area(base, altura=5):
    area = base * altura
    return area
```

- **`base`** es el primer parámetro, que es obligatorio cuando se llama a la función.
- **`altura=5`** es un parámetro con valor por defecto. Si no se pasa un valor para la altura, la función asumirá que la altura es 5.

Ejemplo de uso:
```python
print(calcular_area(10))  # Usará el valor por defecto de altura (5), por lo que dará 10 * 5 = 50
print(calcular_area(10, 3))  # Usará 3 como altura, por lo que dará 10 * 3 = 30
```

#### **Evaluación:**
- **¿Qué sucede si no se pasan argumentos a una función que los requiere?**
  Si llamas a una función y no proporcionas todos los argumentos necesarios, Python generará un error. Este error se conoce como `TypeError`. El mensaje de error indicará que faltan argumentos.

  Ejemplo de error:
  ```python
  def saludar(nombre):
      print(f"Hola, {nombre}!")
  
  saludar()  # Esto causará un error, ya que no se ha pasado el argumento "nombre"
  ```

  **Error generado:**
  ```
  TypeError: saludar() missing 1 required positional argument: 'nombre'
  ```

#### **Resumen:**
1. **Funciones con varios parámetros**: Las funciones pueden aceptar múltiples parámetros, lo que les permite trabajar con diferentes tipos de datos o realizar diversas operaciones.
2. **Argumentos por defecto**: Puedes proporcionar valores predeterminados a los parámetros para que, si no se pasa un valor, la función utilice el valor por defecto.
3. **Errores por falta de argumentos**: Si intentas llamar a una función sin proporcionar los argumentos necesarios, obtendrás un `TypeError`.

Con esta clase, aprendes a trabajar con funciones más flexibles que pueden tener valores predeterminados para algunos de sus parámetros, lo cual es muy útil para simplificar el código y mejorar su legibilidad.