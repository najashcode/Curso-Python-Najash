# la idea es crear un ejercicio que le pida datos al usuario
# estos datos seran: Nombre, edad, telefono
# los datos seran guardados en una lista
# se debe verificar si el usuario es mayor de edad +18 años
# si es mayor se le permite entonces crear un usuario
# este nuevo usuario tendra un usuario y una clave
# y te permitira modificar o actualizar tus datos

nombre = input("Digite su Nombre: ")
edad = input("Digite su edad: ")



if (int(edad)) >= 18 :
    usuario = input("Escriba un nombre de usuario: ")
    clave = input("Digite su nueva clave: ")
    print("Actualizaremos sus datos: ")
    print(" Sus datos actuales son: ")
    datos = [nombre, edad]
    print(datos)
    telefono=input("Digite su numero de Telefono: ")
    datos.append(telefono)
    print(datos)
else: print("No cumple con los requisitos de edad")