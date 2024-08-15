'''
La función fizzbuzz va a recibir un número entero mayor o igual 1.
luego va a imprimir todos los números enteros comenzando en 1 y terminando en el n.
Si el número es múltiplo de 3, en vez de imprimir el número va a imprimir fizz
Si el número es múltiplo de 5, en vez de imprimir el número va a imprimir buzz
Si em número es múltiplo de 3 y 5 a la vez, entonces en vez del número va a imprimir fizzbuzz
'''
def fizzbuzz(n):
    indice = 1
    while indice <= n:
        if (indice % 3 == 0 and indice % 5 == 0):
            print("fizzbuzz")
        elif indice % 3 == 0:
            print("fizz")
        elif indice % 5 == 0:
            print("buzz")
        else:
            print("numero:", indice)
        indice += 1

def fizzbuzz2(n):
    for indice in range(1, n + 1):
        if (indice % 3 == 0 and indice % 5 == 0):
            print("fizzbuzz")
        elif indice % 3 == 0:
            print("fizz")
        elif indice % 5 == 0:
            print("buzz")
        else:
            print("numero:", indice)