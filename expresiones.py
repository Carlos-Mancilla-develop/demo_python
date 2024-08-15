num = -1

if num > 0:
    print("Número positivo")
elif num == 0 :
    print("Cero")
else :
    print("Número negativo")

match num:
    case 0:
        print("match Cero")
    case 1:
        print("match uno")
    case _:
        print("match otro número")

print()
# bucle for

fruits = ["apple", "banana", "cherry"]
for f in fruits:
    print("f:", f)

print()
# iteración en un string
for x in fruits[1]:
  print("x:", x)

print("type(fruits[1]):", type(fruits[1]))
print("fruits[2][5]:", fruits[2][5])

print()
# uso de break para cortar la ejecución de un ciclo for
for f in fruits:
    if f == "banana":
        break
    print("f:", f)

print()
# uso de continue para saltar la ejecución de instrucciones dentro del for, después del continue
for f in fruits:
    print("f:", f)
    if f == "banana":
        continue
    print("f:", f)

print()                   
# uso de else en ciclo for
for x in range(6):
  print("x:", x)
else:
  print("Finally finished!")  

print()
# uso de break y else en ciclo for
for x in range(6):
  if x == 3: 
    break
  print("x:", x)
else:
  print("Finally finished!")   

print()
# uso de ciclos for anidados
adj = ["red", "big", "tasty"]

for a in adj:
  for f in fruits:
    print("a:", a, "f:", f) 

print()
# uso de range, con distintas opciones
lista1 = list(range(5)) # solo un número, genera una secuencia que comienza 0 hasta el numero - 1
print("lista1:", lista1)

print()
# uso de range con el inicio y término de la secuencia, el segundo número no se incluye en la secuencia
lista2 = list(range(1, 11))
print("lista2:", lista2)  

print()
# uso de range con inicio, término de secuencia más el incremento
lista3 = list(range(1, 11, 2))
print("lista3:", lista3) 

print()
# Uso de While
i = 1
while i < 6:
  print("i:", i)
  i += 1
else:
  print("i is no longer less than 6")

x = False
while x:
   print("True") # acá no se ejecuta porque la condición es False

print()
i = 1
while True:
  if i == 6:
    break
  print("i:", i)
  i += 1
else:
  print("i is no longer less than 6")

print()
i = 0
while i < 10:
  i += 1
  if i == 6:
    continue
  print("i:", i)
else:
  print("i is no longer less than 10")

print()
# Revisión de múltiples condiciones con if
numero = int(input("Ingrese número entero del 1 al 10 o 20 al 30: \n"))
if ((numero > 0 and numero <= 10) or (numero >= 20 and numero <= 30)):
  print("Número válido")
else:
  print("Número inválido")

if numero > 19:
  print(" Número es mayor que 10!")
elif numero < 10:
  print("Número es menor que 10!")
elif numero < 20 and numero != 10 :
  print("Número es menor que 20!")
else:
  print("Número es igual a 10")

# vamos a ocupar la misma variable número que viene de antes
if numero >= 0:
  if numero == 0:
    print("Cero")
  else:
    print("Número positivo")
else:
  print("Número negativo")

print()
# condiciones múltiples 
var1 = 3
var2 = 7
var3 = -4

if var1 > 0 and var2 > 0 and var3 > 0 :
  print("Todas las variables son positivas.")
else:
  print("No todas las variables son positivas")

if var1 > 0 or var2 > 0 or var3 > 0 :
  print("Algunas las variables son positivas.")
else:
  print("Todas las variables son negativas o cero.")

print()
# condiciones en una sola línea
i = 16
if i < 20 : print("Es menor a 20")

print(True) if i < 15 else print(False)

print()
# ejemplo for

tupla = (10, 20, 30, 40, 50)
for elemento in tupla:
  print("Índice "+ str(tupla.index(elemento)) + ":", elemento)

# otro ejemplo de for con lista de tuplas
lista_tuplas = [(1, 2), (3, 4), (5, 6)]
for a, b in lista_tuplas:
  print(a, "más", b, "igual", a + b)

for a in lista_tuplas:
   print("a:", a)

for (a, b) in lista_tuplas:
   print("a:", a, "b:", b)

print()
lista_tuplas2 = [(1, 2, 3), (3, 4, 5), (5, 6, 7)]
for a in lista_tuplas2:
   print("a:", a)

for (a, b, c) in lista_tuplas2:
   print("a:", a, "b:", b, "c:", c)

print()
# iteración en un diccionario
diccio = {
  "nombre": "Juan",
  "apellido": "Perez"
}

for clave, valor in diccio.items():
   print("clave:", clave)
   print("valor:", valor)

print()
# iteración sobre un string
cadena_de_texto = "Ciencia es para todos"
print("cadena_de_texto:", cadena_de_texto)
for caracter in cadena_de_texto:
  print(caracter)

print()
# iteracion for con bloque else
digitos = [0, 1, 5]
for i in digitos:
  print("i:", i)
  if (i == 1):
    break
else:
 print("No quedan elementos en la lista.")

print("después del for")

