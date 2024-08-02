from matematica.aritmetica import sumar 

###
# mostrar captura de valores desde terminal (entrada estándar)
###
# username = input("Enter username: ")
# print("Username is: " + username)

decimal = 4.2e-4
decimal2 = 3.00056
print("decimal:", decimal)
print("decimal2:", decimal2)
print(f"decimal2: {decimal2:.2f}")

price = 59
txt = f"El precio es {price:.2f} dólares"
print(txt)

cadena = 'Un texto con "Comillas dobles"'
print(cadena)
cadena = "Un texto con 'Comillas simples'"
print(cadena)
cadena = "Un texto con \"Comillas dobles\" envuelto en comillas dobles \ndesplegado en dos líneas"
print("largo cadena:", len(cadena))
print(cadena)
print(cadena.upper())
print(cadena.lower())
print(cadena)

'''
primer_numero = input("Ingrese primer número entero: ")
print("El tipo de dato de primer_numero es:", type(primer_numero))
primer_numero_entero = int(primer_numero)
print("El número ingresado es:" , primer_numero_entero)
print("El tipo de dato de primer_numero_entero es:", type(primer_numero_entero))

segundo_numero = input("Ingrese segundo número entero: ")
segundo_numero_entero = int(segundo_numero)
print("El número ingresado es:" , segundo_numero_entero)
# La función sumar viene del import en la primera línea
print(f"La suma de los dos numeros es {sumar(primer_numero_entero, segundo_numero_entero)}")
'''

#################### LISTAS ######################
#Una lista de enteros
mi_lista = [1, 2, 3]
print("mi_lista:", mi_lista)
print("primer elemento de mi_lista:", mi_lista[0])
mi_entero: int = 0
print("mi_entero:", mi_entero)
mi_entero = "hola"
print("mi_entero:", mi_entero)

#Otra lista
otra_lista = [4, 5.28, "tercer elemento", [1, 2, 3]]
print("otra_lista:", otra_lista)
print("segundo elemento de otra_lista:", otra_lista[1])
print("cuarto elemento de otra_lista:", otra_lista[3])
print("el segundo elemento del cuarto elemento de otra_lista:", otra_lista[3][1])
lista_interna = otra_lista[3]
print("lista_interna:", lista_interna)
print("el segundo elemento de lista_interna:", lista_interna[1])

# Una lista como variable asignada a otra lista
otra_lista2 = [4, 5.28, "tercer elemento", mi_lista]
print("otra_lista2:", otra_lista2)
print("segundo elemento de otra_lista2:", otra_lista2[1])
print("cuarto elemento de otra_lista2:", otra_lista2[3])
print("cuarto elemento de otra_lista2:", otra_lista2[-1])

# Sobreescribir valor de un elemento de la lista
otra_lista[1] = "M"
print("otra_lista:", otra_lista)
# Como recomendación no es conveniente cambiar el tipo de datos del elemto de la lista
# Por lo que vamos a escribir un valor decimal
otra_lista[1] = 3.14
print("otra_lista:", otra_lista)
print("largo de otra_lista:", len(otra_lista))
# las funciones o métodos que aparecen con doble guión bajo __ son built-in fuctions
# la funcion dir a continuación muestra las funciones que aplican o tiene las listas 
# incluyendo las built-in fuctions que aparecen escritas con __. Pero al usarlas se
# ocupan sin __. Por ejemplo aparece __len__, pero se ocupa len()
#print("información de otra_lista:", dir(otra_lista))

# Si hago esto aparece error por índice fuera de rango
#otra_lista[4] = "Extra"

otra_lista.append("Extra")
print("otra_lista:", otra_lista)
print("largo de otra_lista:", len(otra_lista))

otra_lista.remove("tercer elemento")
print("otra_lista:", otra_lista)
print("largo de otra_lista:", len(otra_lista))

otra_lista.append(0)
otra_lista.append("Extra")
print("otra_lista:", otra_lista)
print("largo de otra_lista:", len(otra_lista))

otra_lista.remove("Extra")
print("otra_lista:", otra_lista)
print("largo de otra_lista:", len(otra_lista))

indice = otra_lista.index("Extra")
print("indice de 'Extra':", indice)

# lanza excepción ya que el elemento no está en la lista, 
# por lo que se debe capturar esta excepción. Lo vamos a ver más adelante
#indice2 = otra_lista.index("tercer elemento")
#print("indice2:", indice2)

print("")
ultimo = otra_lista.pop()
print("ultimo:", ultimo)
print("otra_lista:", otra_lista)
print("largo de otra_lista:", len(otra_lista))

##################### DICCIONARIOS ################
print("")
mi_diccionario = {
    1: 'manzana', 
    2: 'pelota'
}
print("mi_diccionario:", mi_diccionario)
print("segundo elemento en mi_diccionario:", mi_diccionario[2])
print()
mi_diccionario2 = {'nombre': 'Daniel', 'edad': 26}
print("mi_diccionario2:", mi_diccionario2)
print("nombre en mi_diccionario2:", mi_diccionario2["nombre"])
print("edad en mi_diccionario2", mi_diccionario2.get('edad'))
print()
# agregando un elemento al diccionario
mi_diccionario2["rut"] = "11111111-1"
print("mi_diccionario2:", mi_diccionario2)

# para eliminar un elemento del diccionario tenemos tres formas de hacerlo
print()
# Primer método usando pop() se extrae valor contenido en la clave 
# antes de eliminarlo del diccionario
# nota: la asignación a una variable no es obligatorio
edad = mi_diccionario2.pop("edad") 
print("edad:", edad)
print("mi_diccionario2:", mi_diccionario2)
# segundo método usando popitem(), se extrae el último item completo (tupla) 
# antes de eliminarlo del diccionario
# nota: la asignación a una variable no es obligatorio
print()
ultimo_elemento_dic = mi_diccionario2.popitem()
print("ultimo_elemento_dic:", ultimo_elemento_dic)
print("mi_diccionario2:", mi_diccionario2)
# tercer método usando built-in function del. En este caso no hay asignación.
print()
del mi_diccionario2["nombre"]
print("mi_diccionario2:", mi_diccionario2)

############ TUPLAS #################
print()
mi_tupla = (1, 2, 3)
print("mi_tupla:", mi_tupla)
# tupla con tipos de datos mixtos
mi_tupla2 = (1, "Hola", 3.4)
print("mi_tupla2:", mi_tupla2)
# acceder al segundo elemento de mi_tupla2, se usan índices al igual que en las listas
print()
print("segundo elemento de mi_tupla2:", mi_tupla2[1])
print("El tamaño de mi_tupla2 es:", len(mi_tupla2))

# creando una tupla con un solo elemento
print()
thistuple = ("apple",)
print(type(thistuple))

#NO es una tupla
thistuple2 = ("apple")
print(type(thistuple2))

# creando una tupla usando constructor de tupla. Built-in fuction tuple()
thistuple3 = tuple(("apple"))
print(type(thistuple3))

############### SET (o conjunto) ###################
print()
# conjunto de enteros
mi_conjunto = {1, 2, 3}
print("mi_conjunto:", mi_conjunto)
print(type(mi_conjunto))

print()
# Crear un set vacío
que_es = set()
print("que_es:", que_es)
print(type(que_es))
