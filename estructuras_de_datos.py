x = ('apple', 'banana', 'cherry')
y = enumerate(x)
print("x:", x)
print("y:", y)

for i, f in enumerate(x):
    print("i:", i, "f:", f)

for e in y:
    print("e:", e)

print()
# Vamos a revisar conjuntos (set)
lista_con_repetidos = [1, 2, 3, 2, 4, 3, 3, 2, 5]
set_desde_lista = set(lista_con_repetidos)
lista_sin_repetidos = list(set_desde_lista)
print("lista_con_repetidos:", lista_con_repetidos)
print("set_desde_lista:", set_desde_lista)
print("lista_sin_repetidos:", lista_sin_repetidos)

print()
mi_set = {'london', 'new york', 'seattle', 'sydney'}
mi_lista = list(mi_set)

for indice, valor in enumerate(mi_set, 1):
    print(f"mi_set, indice: {indice} - valor: {valor}")

# print(f"lista_sin_repetidos[0]: {lista_sin_repetidos[0]}")
# print(f"set_desde_lista[0]: {set_desde_lista[0]}") # Esto lanza error ya que un set no es indexado

print()
# vamos a probar set con función iter()
for item in iter(mi_set):
    print("item:", item)

print()

# enumerate de mi_lista que fue creada a partir de un set
for indice, valor in enumerate(mi_lista, 1):
    print(f"mi_lista, indice: {indice} - valor: {valor}")

print("mi_lista[0]:", mi_lista[0])

print()
mi_set2 = {'london', 'new york', 'seattle', 'sydney'}
for item in iter(mi_set):
    print("iter(mi_set), item:", item)
for item in iter(mi_set2):
    print("iter(mi_set2), item:", item)

print()

for item in mi_set:
    print("mi_set, item:", item)
for item in mi_set2:
    print("mi_set2, item:", item)

print()
# trabajo con diccionarios
paises_y_capitales = {
    'Japon': 'Tokio', 
    'Inglaterra': 'Londres', 
    'Francia': 'Paris', 
    'Alemania': 'Berlin'
}

keys = paises_y_capitales.keys()

for clave in keys :
    print(f"{clave} - {paises_y_capitales[clave]}")

print()
items = paises_y_capitales.items()

for item in items:
    print(f"item: {item} - paises_y_capitales[item[0]]: {paises_y_capitales[item[0]]}")
    print(f"item: {item} - clave: (item[0]): {item[0]} - valor: (item[1]): {item[1]}")

print()
paises_y_capitales['Chile'] = 'Santiago'
for pais in paises_y_capitales:
    print(f"{pais} - {paises_y_capitales[pais]}")

print()
# busqueda de clave dado su valor, esto aplica desde python 3.7
# obtengo la lista de claves (keys)
# ahora vamos a obtener una lista de valores (values)
keys = list(paises_y_capitales.keys())
values = paises_y_capitales.values()

for indice, valor in enumerate(values):
    # obtener la clave del valor
    print(f"valor: {valor} - clave: {keys[indice]}")