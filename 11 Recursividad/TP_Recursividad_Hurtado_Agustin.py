# Definición de funciones
#1
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def calcular_factoriales_hasta_n(n):
    for i in range(1, n+1):
        print(f"El factorial de {i} es {factorial(i)}")

#2
def fibo_recur(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibo_recur(pos - 1 ) + fibo_recur(pos - 2)

def mostrar_serie_fibonacci(n):
    serie = [fibo_recur(i) for i in range(n)]
    for i, valor in enumerate(serie):
        print(f"Fibonacci en la posición {i} es {valor}")    

#3
def potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / potencia(base, -exponente)
    else:
        return base * potencia(base, exponente - 1)

#4
def decimal_a_binario(n):
    if n < 2:
        return str(n)
    else:
        return decimal_a_binario(n // 2) + str(n % 2)
    
#5
def es_palindromo(palabra):
    # Caso base: si la palabra tiene 0 o 1 carácter, es palíndromo
    if len(palabra) <= 1:
        return True
    # Compara el primer y último carácter
    if palabra[0] != palabra[-1]:
        return False
    # Llama recursivamente con la subcadena sin el primer y último carácter
    return es_palindromo(palabra[1:-1])    

#6
def suma_digitos(n):
    if n == 0:
        return 0
    else:
        return (n % 10) + suma_digitos(n // 10)
    
#7    
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)
    
#8
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        # Compara el último dígito con el dígito buscado y suma 1 si coinciden
        cuenta_actual = 1 if (numero % 10) == digito else 0
        return cuenta_actual + contar_digito(numero // 10, digito)    

# Programa principal
#1
numero_usuario = int(input("Introduce un número entero: "))
calcular_factoriales_hasta_n(numero_usuario)

#2
numero_usuario = int(input("Introduce la posición hasta la que deseas ver la serie de Fibonacci: "))
mostrar_serie_fibonacci(numero_usuario)

#3
base = float(input("Introduce la base: "))
exponente = int(input("Introduce el exponente (entero): "))

resultado = potencia(base, exponente)
print(f"{base} elevado a {exponente} es {resultado}")

#4
numero = int(input("Introduce un número entero positivo: "))
binario = decimal_a_binario(numero)
print(f"El número {numero} en binario es {binario}")

#5
texto = input("Introduce una palabra sin espacios ni tildes: ").lower()
if es_palindromo(texto):
    print(f"La palabra '{texto}' es un palíndromo.")
else:
    print(f"La palabra '{texto}' no es un palíndromo.")

#6
numero = int(input("Introduce un número entero positivo: "))
resultado = suma_digitos(numero)
print(f"La suma de los dígitos de {numero} es {resultado}")

#7
nivel_inferior = int(input("Introduce el número de bloques en el nivel más bajo: "))
total = contar_bloques(nivel_inferior)
print(f"El total de bloques necesarios es {total}")

#8
num = int(input("Introduce un número entero positivo: "))
dig = int(input("Introduce el dígito a contar (0-9): "))
resultado = contar_digito(num, dig)
print(f"El dígito {dig} aparece {resultado} veces en el número {num}.")