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