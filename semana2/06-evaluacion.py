"""Día 6: Evaluación práctica
- **Ejercicio**:
- Crea un programa que permita gestionar una lista de contactos (nombre, número de teléfono) 
usando listas y diccionarios.
- **Evaluación**:
- Presenta tu gestión de contactos y explica cómo funciona."""

nombre = input("Digite su Nombre: ")
telefono = input("Digite su numero de telefono:")

#datos = (nombre, telefono)

#print (datos)

usuario = {
    "nombre" : nombre,
    "telefono" : telefono
}

print (f"El Usuario encontrado es: {usuario["nombre"]}")
"""
datos = (usuario["nombre"])
print(datos)"""