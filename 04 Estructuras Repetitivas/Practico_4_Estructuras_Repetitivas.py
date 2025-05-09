#1

"""for i in range(101):
    print(i)
    """

#2
"""
num = input("Ingresa un número entero: ")

if num.startswith('-'):
    num = num[1:]
cantidad_digitos = len(num)

print(f"El número ingresado tiene {cantidad_digitos} dígito(s).")

"""

#3
'''
a = int(input("Ingresa el primer número entero: "))
b = int(input("Ingresa el segundo número entero: "))

menor = min(a, b)
mayor = max(a, b)

suma = 0
for num in range(menor + 1, mayor):
    suma += num

print(f"La suma de los números enteros entre {a} y {b}, excluyéndolos, es: {suma}")
'''

#4
'''
suma = int(0)
n = int(input("Ingrese un número entero: "))

while n != 0:
    suma += n
    n = int(input("Ingrese un número entero: "))

print(f"El total acumulado es {suma}.")
'''
#5
"""
import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

print("Adivina el número entre 0 y 9")

while adivinado != True:
    entrada = input("Ingresa tu intento: ")

    if entrada.isdigit():
        intento = int(entrada)
        if 0 <= intento <= 9:
            intentos += 1
            if intento == numero_secreto:
                adivinado = True
                print(f"Felicidades, Adivinaste el número en {intentos} intento(s).")
            else:
                print("No acertaste, intenta de nuevo.")
        else:
            print("Por favor, ingresa un número entre 0 y 9.")
    else:
        print("Entrada inválida. Por favor, ingresa un número entero.")
"""        

#6
"""
cont = 100

while cont > 2:
    cont = cont - 2
    print(cont)
"""

#7
"""
n = int(input("Ingresa un número entero positivo: "))
suma = 0
for i in range(n + 1):
    suma += i
print("La suma es:", suma)
"""
#8
"""
pares = 0
impares = 0 
positivos = 0
negativos = 0

for i in range(5):
    num = int(input(f"Ingrese el número entero {i+1}: "))

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

print(f"Pares: {pares}")
print(f"Impares: {impares}")
print(f"Negativos: {negativos}")
print(f"Positivos: {positivos}")
"""

#9
"""
suma = 0

for i in range(5):
    num = int(input(f"Ingrese el número entero {i+1}: "))
    suma += num

print("La media es", (suma/(i+1)))    
"""

#10
"""
numero = input("Ingresa un número: ")
numero_invertido = numero[::-1]
print("Número invertido:", numero_invertido)
"""