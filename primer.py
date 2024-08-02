from matematica.aritmetica import sumar as sum

print("Hola Mundo!!!")

cadena = "Esta es una cadena de texto"
print(cadena)

if True:
    print("True")

# Este es un comentario de una sola línea

''' 
Este es un comentario 
multilínea
'''

"""
Este también es un comentario 
multilínea
"""

# print(dir(cadena))
suma = sum(3,4)
print("La suma es:", suma)
txt = f"La suma es: {suma}"
print(txt)

print((2 + 3) * 5)


a = b = c = 300
print(a, b, c)

#variable global
s = "esta es una variable global"

def f():
    #variable local
    global s
    s = "esta es una variable local"
    print("s:", s)
    s = "esta es una variable local de nuevo"
    print("s:", s)

f()
print("s:", s)
s = "esta es una variable global de nuevo"
print("s:", s)

