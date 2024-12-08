try:
    numero = int(input("Ingresa un numero: "))
    print(f"Has ingresado el numero {numero}.")
except ValueError:
    print("Error!: Debes ingresar un valor numerico")

try:
    resultado = 10 / "cinco"
except Exception as e:
    print(f"Ocurrió un error: {e}")


try:
    archivo = open("archivo.txt", "r")
    contenido = archivo.read()
    numero = int(contenido)
except (FileNotFoundError, ValueError) as e:
    print(f"Error: {e}")
