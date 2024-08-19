a = 5
b = 10
iteraciones = 5
cuenta = 0
while cuenta < a or cuenta < b and not cuenta >= iteraciones:
    print(f"Cuenta: { cuenta }, a: {a}, b: {b}")
    cuenta += 1

print()
# Probando ciclos infinitos
i = 0
while i <= 10:
    print("He creado un ciclo infinito")
    i += 3 # si no está esta línea, el ciclo se ejecuta sin fin

print()
# probando bucles anidados
for i in range(5):
    print(f"en for externo i: {i}")
    for j in range(i):
        print("*", end="")
        # print(f"i: {i} - j: {j}")
    print("")

print()
i = 1
while(i <= 5):
    j = 5
    while(j >= i):
        print(j, end=' ')
        j -= 1
    i += 1
    print()

print()
# Pruebas de break y continue en bucle for
estudiantes = ["Paul", "Luis", "Carmen", "Alicia"]

for estudiante in range(len(estudiantes)):
    if estudiante == 2:
        continue # cambiar continue por break para ver la diferencia
    else:
        print(f"estudiantes[{estudiante}]: {estudiantes[estudiante]}")
    print(f"estudiante es {estudiante}")

print("Fuera del for")

print()
# multiples condiciones con while
a = 5
b = 10
contador = 0

while contador < a and contador < b:
    print(f"cuenta: {contador}, a: {a}, b: {b}")
    contador += 1

contador = 0
print()

while contador < a or contador < b:
    print(f"cuenta2: {contador}, a: {a}, b: {b}")
    contador += 1

print()
# Iterando sobre un diccionario
acciones = {
    'AAPL': 187.31,
    'MSFT': 124.06,
    'FB': 183.50
}

for clave, valor in acciones.items() :
    print(clave + " : " + str(valor))
    print(f"{clave} : {valor}")

print()

for item in acciones.items():
    print(f"{item[0]} : {item[1]}")