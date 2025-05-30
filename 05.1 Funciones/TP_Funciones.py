import math
# Definición de funciones
def imprimir_hola_mundo():
    print("Hola Mundo!")

def saludar_usuario(nombre):
    print(f"Hola {nombre}!")

def informacion_personal(nombre, apellido, edad, residencia):  
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")  

def calcular_area_circulo(radio):
    return math.pi * (radio * radio)

def calcular_perimetro_circulo(radio):
    return math.pi * (radio * 2)

def segundos_a_horas(segundos):
    return segundos/3600

def tabla_de_multiplicar(num):
    print(f"La tabla del {num} es:")
    for i in range(1,11):
        resultado = num * i
        print(f"{num} x {i} = {resultado}")

def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        division = None
    return (suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc

def celsius_a_fahrenheit(temp_celcius):
    temp_fahrenheit = (temp_celcius * (9/5)) + 32
    return temp_fahrenheit

def calcular_promedio(a, b, c):
    promedio = (a + b + c) / 3
    return promedio

# Programas principales

#1 
imprimir_hola_mundo()

#2
nombre = input("Ingresa tu nombre: ")
saludar_usuario(nombre)

#3
nombre1 = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
edad = int(input("Ingresa tu edad: "))
residencia = input("Ingresa tu residencia: ")
informacion_personal(nombre1, apellido, edad, residencia)

#4 
radio = float(input("Ingrese el radio del círculo: "))
area = calcular_area_circulo(radio)
perimetro = calcular_perimetro_circulo(radio)
print(f"El área del círculo es {area} y el perímetro es {perimetro}")

#5
segundos = float(input("Ingrese una cantidad de segundos: "))
horas = segundos_a_horas(segundos)
print(f"{segundos} segundos son equivalentes a {horas} horas. ")

#6
num = int(input("Ingrese un número para conocer su tabla de multiplicar: "))
tabla_de_multiplicar(num)

#7
num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
resultados = operaciones_basicas(num1, num2)

print(f"Suma: {resultados[0]}")
print(f"Resta: {resultados[1]}")
print(f"Multiplicación: {resultados[2]}")
if resultados[3] is not None:
    print(f"División: {resultados[3]}")
else:
    print("División: No se puede dividir por cero.")

#8
peso = float(input("Ingresa tu peso en kilogramos: "))
altura = float(input("Ingresa tu altura en metros: "))

imc = calcular_imc(peso, altura)
print(f"Tu indice de masa corporal (IMC) es {imc}.")

#9
temp_celcius = float(input("Ingresa la temperatura en grados Celsius: "))
temp_fahrenheit = celsius_a_fahrenheit(temp_celcius)
print(f"{temp_celcius} grados Celsius equivalen a {temp_fahrenheit} grados Fahrenheit")

#10
numa = float(input("Ingresa el primer número: "))
numb = float(input("Ingresa el segundo número: "))
numc = float(input("Ingresa el tercer número: "))

resultado = calcular_promedio(numa, numb, numc)
print(f"El promedio de los tres números es: {resultado}")