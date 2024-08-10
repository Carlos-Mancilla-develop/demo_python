# operadores lógicos

x = True
y = False

print("x or y es:", x or y)

print()
# Operadores de comparación
x = 10
y = 12
z = "10"

print(f"x: {x}, y: {y}, z: {z}")
print("x > y es:", x > y)
print("x == z es:", x == z)
print("x != z es:", x != z)

print()
# Tipos de datos de las variables u objetos
print("type(x):", type(x))
print("type(y):", type(y))
print("type(z):", type(z))

print()
# conversión de tipos de datos implícita
a = 1
b = 2.14
print("type(a):", type(a))
print("type(b):", type(b))
# a = a + b
a += b
print("type(a):", type(a))
print("a:", a)

print()
# conversión explícita de datos (cast o casting)
print(f"x: {x}, y: {y}, z: {z}")
print(f"x + z = {str(x) + z}")
print(f"x + z = {x + int(z)}")
print(f"x * z = {x * z} (caso curioso, cuidado!!)")
print(f"x * z = {x * int(z)}")