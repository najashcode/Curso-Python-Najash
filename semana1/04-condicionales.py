""" 5. **Día 5: Condicionales (if, else, elif)**
- Estructura condicional.
- Ejercicios con condiciones sencillas.


Día 5: Condicionales (if, else, elif)
- **Teoría**:
- Estructura condicional `if`, `elif`, `else`.
- Ejemplos de condiciones anidadas.
"""

# USO DEL IF

# En todos los casos de la vida real como en la programacion existen 
# algoritmos que estan condicionados por una orden o contra orden.

"""En el caso de Python estas condiciones afectan el funcionamiento de un 
programa decidiendo que hacer y que no.

En Casi todos los lenguajes de programacion tenemos condicionales if que
no es otra cosa que en ingles preguntar ¿y si?.

por ejemplo, un niño que quiere subir a una atraccion en un parque de diversiones
tendra que pasar por una vara de medicion que determinara si tiene la 
altura indicada para tal atraccion. En este caso la altura debe ser 140cms

si el niño tiene 140cms o mas, puede ingresar a la atraccion, sino, debe salir de la fila

Ahora hagamos esto en codigo"""

"""estatura = input("Digite la estatura del niño: ")
if (int(estatura)) >= 150 :
    print("Puede ingresar al parque")

# seguro que el niño estara triste, por lo tanto le daremos la opcion de
# ir a otro lugar si la estatura no es la correcta.
# USO DEL ELIF
elif (int(estatura)) >= 140 :
    print("El niño puede Jugar en los video Juegos")

else:print ("Puede intentar en el Juego de las moticos")"""

"""- **Ejercicio**:
- Crea un programa que pida la edad del usuario y determine si es menor, mayor o igual a 18 años.
- **Evaluación**:
- Explica la diferencia entre `if` y `elif`."""
usuario = input("Digite su nombre de usuario: ")
edad = input("digite su edad: ")

if (int(edad)) >= 18 :
    print (f"{usuario} es mayor de edad")
else:print (f"uy {usuario} Todavia te faltan algunos años")

