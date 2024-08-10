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