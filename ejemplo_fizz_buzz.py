from fizzbuzz.ejecucion import fizzbuzz, fizzbuzz2
from os import system, name as os_name
from time import sleep

def limpia_pantalla():
    if os_name == 'nt':
        system("cls")
    else:
        system("clear")

continuar = "s"
while continuar == "s":
    limpia_pantalla()
    n = int(input("Ingrese número entero mayor a 1 \n"))
    if n >= 1:
        fizzbuzz(n)
        print("*****************")
        fizzbuzz2(n)
    continuar = input("Desea continuar (s/n)\n").lower()
    print("continuar:", continuar)
    sleep(3)






