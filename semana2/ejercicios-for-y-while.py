"""Ejercicio 1: Practicar for y while
Ciclo for: Imprime los números del 1 al 10.
"""
print ("-- Ejercicio For --")
for num in range(1,11):
    print (num)

#Ciclo while: Crea un ciclo que imprima los números del 1 al 10, pero usando while.
print ("-- Ejercicio While --")
numero = 0
while numero <= 10:
    print (numero)
    numero += 1

#Ejercicio 2: Usar ambos ciclos juntos

#Imagina que tienes una lista de productos
#  en una tienda, y quieres usar un ciclo 
# for para iterar sobre los productos, 
# pero un ciclo while para detener la iteración
#  si encuentras un producto agotado.

productos = ["camisa", "pantalon", "zapato", "agotado"]

for producto in productos:
    if producto == "agotado":
        print("EL producto no se encuentra disponible, Deteniendo Busqueda")
        break
    print(f"Producto encontrado: {producto}")

