# 1. Variables y conversión de tipos
nombre = input("Ingrese el nombre del producto: ")
precio = float(input("Ingrese el precio del producto: "))
cantidad = int(input("Ingrese la cantidad en stock: "))
disponible = input("¿Está disponible? (True/False): ").strip().lower() == 'true'

# 2. Diccionario del producto
producto = {
    "nombre": nombre,
    "precio": precio,
    "cantidad": cantidad,
    "disponible": disponible
}

# 3. Lista de inventario y bucle para múltiples productos
inventario = [producto]
for _ in range(3):
    nombre = input("Ingrese el nombre del siguiente producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad en stock: "))
    disponible = input("¿Está disponible? (True/False): ").strip().lower() == 'true'
    
    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad,
        "disponible": disponible
    }
    inventario.append(producto)

# 4. Función de consulta de precio
def consultar_precio(nombre_producto):
    for prod in inventario:
        if prod["nombre"] == nombre_producto:
            print(f"El precio de {nombre_producto} es: {prod['precio']}")
            return
    print("Producto no encontrado en el inventario.")

nombre_producto = input("Ingrese el nombre del producto para consultar el precio: ")
consultar_precio(nombre_producto)

# 5. Cálculo del valor total del inventario
valor_total = sum(prod["precio"] * prod["cantidad"] for prod in inventario)
print(f"El valor total del inventario es: {valor_total}")

# 6. Tuplas y conjuntos
productos_disponibles = tuple(prod["nombre"] for prod in inventario)
precios_unicos = set(prod["precio"] for prod in inventario)

# 7. Mostrar resultados
print("\nInventario completo:")
for prod in inventario:
    print(f"Nombre: {prod['nombre']}, Precio: {prod['precio']}, Cantidad: {prod['cantidad']}, Disponible: {prod['disponible']}")

print(f"\nLista de productos disponibles: {productos_disponibles}")
print(f"Conjunto de precios únicos: {precios_unicos}")
