"""
Día 3: Operadores matemáticos y lógicos
- **Teoría**:
- Operadores matemáticos: `+`, `-`, `*`, `/`, `//`, `%`, `**`.
- Operadores lógicos: `and`, `or`, `not`.
- Operadores de comparación: `==`, `!=`, `<`, `>`, `<=`, `>=`.

"""
#Operadores Matematicos
"""Las matematicas se dan bien en python. Con solo escribir algun operador
matematico ya hemos convertido nuestro codigo en una calculadora"""
print("*********************************")
print(" ** Operadores Matemaricos ** ")
print("*********************************")
print (2+2)

suma = 2 + 2
print (suma)

resta = 5 - 2
print(resta)

division = 10 / 2
print (division)

division_exacta = 10 // 2
print(division_exacta)
print (type(division))
print(type(division_exacta))

modulo = 25 % 2
print(modulo)

exponente = 3**5
print(exponente)

# Operadores Logicos
"""Son aquellos que condicionan un algoritmo, por ejemplo, quiero hacer esto
si tengo esto Y (and) esto, o quiero hacer esto si tengo esto O (or) esto, o 
quiero hacer esto si NO (not) tengo esto"""
print("*********************************")
print(" ** Operadores Logicos ** ")
print("*********************************")
# and
edad = 18
nombre = "Danny"
if edad == 18 and nombre == "Danny" : #Aqui verifica que edad sea si o si igual a 17
    #aqui se utiliza el doble igual porque la comparacion tiene que ser exacta y 
    #valida que nombre si o si sea igual a Danny
    print("el Y se cumple") #si las condiciones se cumplieran imprimiria
else : print("No coincide") #sino se cumple imprime esto
"""En este caso va a imprimir no coincide ya que edad no es 17 sino 18"""

#OR
if edad == 34 or nombre == "Johanna" :
    print("El OR se cumple")
else : print("No se cumple ninguna de las dos condiciones")
    
""" NOT
stock = int(input('Ingrese el numero de stock: '))

val = not(stock >= 100 and stock <= 1000)
if val == True:
  print("Su pedido sera atendido de inmediato")
else: print("Su pedido no cumple con los requeriminetos")"""

# Operadores de Comparacion
# `==`, `!=`, `<`, `>`, `<=`, `>=`.
# Creo que debimos comenzar por aqui
# en python mientras que el = asigna un valor el doble = compara los valores
print("*********************************")
print(" ** Operadores de Comparacion ** ")
print("*********************************")
asignacion = "Asignamos el valor con el ="
if asignacion == "Asignamos el valor con el =" : #Aqui comparamos los valores
   print("Aqui comparamos los valores ingresados con el de la variable")
else : print("No es igual al valor de la variable")

a =  12
b = 24
if a == 12 and b != 2 :
 print ("Aqui usamos el diferente")
else : print ("Todo esta igual a las variables")

if a < 10 : print ("a es menor")
else : print ("a es mayor")

if a > 10 : print ("a es mayor")
else : print ("a es menor")

if a >= 10 : print ("a es mayor o igual")
else : print ("a es menor")

if a <= 10 : print ("a es menor o igual")
else : print ("a es mayor")


"""
- **Ejercicio**:
- Crea un programa que tome dos números del usuario y muestre los resultados de diferentes operaciones matemáticas y comparaciones.
- **Evaluación**:
- ¿Qué resultado se obtiene al evaluar `True and False`?
"""
numero1 = input("Digite el primer Numero")
numero2 = input("Digite el segundo numero")

arimeticos = numero1 + numero2
print(arimeticos)

if numero1 == numero2 :
   print("Los numeros son iguales")
else: print("Ha introducido numeros diferentes")

verdad = True
mentira = False
print(verdad + mentira)
print (type((verdad + mentira)))

