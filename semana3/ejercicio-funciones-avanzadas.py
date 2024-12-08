contador = 2
print(f"Valor inicial del contador es {contador} ")
def modificar_contador():
    global contador
    contador = contador + 1
    print(f"el Valor modificado del contador es {contador}")

modificar_contador()


productos = [("Laptop", 800), ("Teléfono", 600), ("Tablet", 400)]
productos_ordenados = sorted(productos, key=lambda x: x[1])
print(productos_ordenados)

numeros = [3, 8, 15, 22, 7, 14, 19, 24]
pares = list(filter(lambda x : x%2 == 0, numeros))
print(pares)

numeros = [2, 4, 6, 8, 10]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)
