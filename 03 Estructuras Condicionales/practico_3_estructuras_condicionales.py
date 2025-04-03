from statistics import mode, median, mean
import random

#1
print("Hola")
edad = int(input("Por favor, ingrese su edad: "))
if edad >= 18:
    print("Es mayor de edad")
else:
    print("Usted es menor de edad")  

#2
nota = int(input("Por favor, ingrese su nota: "))
if nota >= 6 and nota <= 10:
    print(f"Usted a sacado un {nota}, esta aprobado.")
elif nota >= 0 and nota < 6:
    print(f"Usted a sacado un {nota}, lamentablemente esta desaprobado.")
else:
    print("Ingrese una nota válida")

#3 
num = int(input("Por favor ingrese un número entero: "))
if num % 2 == 0:
    print(f"Usted ha ingresado el número {num} el cual es par.")
else:
    print("Por favor, ingrese un número par.")

#4
edad1 = int(input("Por favor, ingrese su edad: "))
print(f"Tiene {edad1} años por lo que...")
if edad1 >= 0 and edad1 < 12:
    print("Es usted niño/a")
elif edad1 >= 12 and edad1 < 18:
    print("Es usted adolescente")
elif edad1 >= 18 and edad1 < 30:
    print("Es usted adulto/a joven")
elif edad1 >= 30 and edad1 <= 130:
    print("Es usted adulto/a")
else:
    print("Ingrese una edad válida!!!")
                
#5
contra = input("Por favor ingrese una contraseña: ")
if len(contra) >= 8 and len(contra) <= 14:
    print("La contraseña ingresa es válida.")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres.")

#6
num_aleatorios = [random.randint(1, 100) for i in range(50)]
print(num_aleatorios)

if mean(num_aleatorios) > median(num_aleatorios) and median(num_aleatorios) > mode(num_aleatorios):
    print("La distribución tiene un sesgo positivo.")
elif mean(num_aleatorios) < median(num_aleatorios) and median(num_aleatorios) < mode(num_aleatorios):   
    print("La distribución tiene un sesgo negativo.")
elif mean(num_aleatorios) == median(num_aleatorios) and median(num_aleatorios) == mode(num_aleatorios):
    print("La distribución no tiene sesgo.") 
else:
    print("No se puede determinar.")      

#7 
frase = input("Por favor ingrese una frase o palabra: ")

if len(frase) > 0 and frase[-1].lower() in "aeiouáéíóú":
    frase += "!"
print(frase)   

#8
nombre = input("Por favor ingrese su nombre: ")
opc = int(input("Por favor ingrese 1, 2 o 3 para elegir como desea que se imprima su nombre: "))

if opc == 1:
    nombre = nombre.upper()
elif opc == 2:
    nombre = nombre.lower()
elif opc == 3:
    nombre = nombre.title()
else:
    print("Ingrese una opción válida")
print(nombre)

#9
magnitud = float(input("Por favor ingrese la magnitud del terremoto: "))

if magnitud > 0 and magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado") 
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy fuerte")
else:
    print("Extremo") 

#10
hemisferio = input("Por favor ingrese en que hemisferio se encuentra (N/S): ")
mes = int(input("Por favor ingrese el número del mes del año en el que se encuentra: "))
dia = int(input("Ingrese en que día se encuentra: "))

if hemisferio == "N":
    if mes in (1, 2):
        print("Invierno")
    elif mes == 12 and dia >= 21:
        print("Invierno")
    elif mes == 3 and dia <= 20:
        print("Invierno")
    elif mes in (4, 5):
        print("Primavera")
    elif mes == 3 and dia >= 21:
        print("Primavera")
    elif mes == 6 and dia <= 20:
        print("Primavera")
    elif mes in (7, 8):
        print("Verano")
    elif mes == 6 and dia >= 21:
        print("Verano")
    elif mes == 9 and dia <= 20:
        print("Verano")
    elif mes in (10, 11):
        print("Otoño")
    elif mes == 9 and dia >= 21:
        print("Otoño")
    elif mes == 12 and dia <= 20:
        print("Otoño")            
elif hemisferio == "S":
    if mes in (1, 2):
        print("Verano")
    elif mes == 12 and dia >= 21:
        print("Verano")
    elif mes == 3 and dia <= 20:
        print("Verano")
    elif mes in (4, 5):
        print("Otoño")
    elif mes == 3 and dia >= 21:
        print("Otoño")
    elif mes == 6 and dia <= 20:
        print("Otoño")
    elif mes in (7, 8):
        print("Invierno")
    elif mes == 6 and dia >= 21:
        print("Invierno")
    elif mes == 9 and dia <= 20:
        print("Invierno")
    elif mes in (10, 11):
        print("Primavera")
    elif mes == 9 and dia >= 21:
        print("Primavera")
    elif mes == 12 and dia <= 20:
        print("Primavera")
else:
    print("Elija entre N y S.")