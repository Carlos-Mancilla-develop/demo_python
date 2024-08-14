from fizzbuzz.ejecucion import fizzbuzz
import os

os.system("cls")  # esto es para windows, en mac o linux es clear no cls

n = int(input("Ingrese número entero mayor a 1 \n"))

if n >= 1:
    fizzbuzz(n)

