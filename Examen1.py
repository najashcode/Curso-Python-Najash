"""Imagina que estás creando un programa para gestionar un pequeño inventario de productos.
El programa permitirá ingresar productos con su precio, cantidad en stock y algunas 
características adicionales. 
A continuación, podrás calcular el valor total del inventario, realizar ciertas consultas
y mostrar resultados.

"""

# Creación de variables:

producto = input("Digite el nombre del producto: ") 
precio = float(input("Ingrese el valor del producto: "))
cantidad = int(input("Ingrese la cantidad disponible en Stock: "))
disponible = input("¿Está disponible? (True/False): ").strip().lower() == 'true' # Esta funcion permite que el usuario escriba sin sensibilidad de mayusculas y minusculas

# Creacion del Diccionario

producto = {
    "nombre": producto,
    "precio": precio,
    "cantidad": cantidad,
    "disponible": disponible
}

for clave, valor in producto.items():
    print(clave, ":", valor) # Muestro lo que tengo actualmente en el diccionario

# Creacion de la lista inventario

inventario = [producto] # Creamos una lista que contiene el diccionario producto
cantidad_productos = int(input("¿Cuantos productos nuevos desea ingresar?: "))
if cantidad_productos >= 0:
    for _ in range(cantidad_productos): #Pedimos al usuario que ingrese la cantidad de productos a crear
        nombre = input("Ingrese el Siguiente producto: ") # Pedimos la informacion del siguiente producto
        precio = float(input("Digite el precio del producto: "))
        cantidad = int(input("Digite la cantidad de existencias en stock: "))
        disponible = input("¿Está disponible? (True/False): ").strip().lower() == 'true'

        producto = { # y dentro de este ciclo creamos nuevamente un diccionario llamado producto donde almacenaremos los datos del usuario
            "nombre" : nombre,
            "precio" : precio,
            "cantidad" : cantidad,
            "disponible" : disponible
        }
        inventario.append(producto) # Agregamos a la lista inventario lo que tiene el dicionario producto
else: print("Debe ingresar un numero positivo")

print(inventario) # en este caso yo imprimi la lista para verificar los datos

# Creamos funcion para consultar precio

def consultar_precio (nombre_producto):
    for prod in inventario:
       if prod["nombre"] == nombre_producto:
            print(f"el precio de {nombre_producto} es {prod["precio"]}")
            return
    print("El producto solicitado no esta en la base de datos.")

nombre_producto = input("Ingrese el nombre del producto para consultar el precio: ")
consultar_precio(nombre_producto)

# 5. Cálculo del valor total del inventario
valor_total = sum(prod["precio"] * prod["cantidad"] for prod in inventario)
print(f"El valor total del inventario es:{ valor_total}")