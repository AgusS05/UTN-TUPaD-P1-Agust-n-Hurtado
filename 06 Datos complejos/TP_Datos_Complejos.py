# Agustín Hurtado
#1 
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300
print(precios_frutas)

#2
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800
print(precios_frutas)

#3
frutas = list(precios_frutas.keys())
print(frutas)

#4
agenda = {}
for i in range(5):
    nombre = input("Nombre del contacto: ")
    numero = input("Número de teléfono: ")
    agenda[nombre] = numero

consulta = input("¿De quién querés saber el número? ")
if consulta in agenda:
    print("El número es:", agenda[consulta])
else:
    print("No existe ese contacto.")

#5
frase = input("Ingresá una frase: ")
palabras = frase.split()
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

frecuencia = {}
for palabra in palabras:
    if palabra in frecuencia:
        frecuencia[palabra] += 1
    else:
        frecuencia[palabra] = 1
print("Frecuencia de palabras:", frecuencia)

#6
for i in range(3):
    nom = input("Nombre del alumno: ")
    notas = input("Ingresá 3 notas separadas por espacio: ").split()
    notas = tuple(map(float, notas))
    promedio = sum(notas) / 3
    print(f"{nom}: promedio = {promedio}")

#7
parcial1 = {1, 2, 3, 4, 5}
parcial2 = {4, 5, 6, 7}

ambos = parcial1 & parcial2
solo_uno = parcial1 ^ parcial2
al_menos_uno = parcial1 | parcial2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno:", solo_uno)
print("Aprobaron al menos uno:", al_menos_uno)

#8
stock = {'arroz': 10, 'fideos': 5, 'azúcar': 8}
producto = input("Producto a consultar: ")

if producto in stock:
    print("Stock actual:", stock[producto])
    agregar = input("¿Querés agregar unidades? (s/n): ")
    if agregar.lower() == 's':
        cantidad = int(input("¿Cuántas unidades? "))
        stock[producto] += cantidad
else:
    print("Producto no encontrado. Se agregará al stock.")
    cantidad = int(input("¿Cuántas unidades? "))
    stock[producto] = cantidad

print(stock)

#9
agenda = {('miercoles', '11:00'): 'Gimnasio', ('jueves', '15:00'): 'Terapia'}
dia = input("Día a consultar: ")
hora = input("Hora a consultar: ")
clave = (dia, hora)
if clave in agenda:
    print("Actividad:", agenda[clave])
else:
    print("No hay actividad programada.")

#10
paises_capitales = {'Argentina': 'Buenos Aires', 'Brasil': 'Brasilia', 'Chile': 'Santiago', 'Peru': 'Lima'}
capitales_paises = {}
for pais, capital in paises_capitales.items():
    capitales_paises[capital] = pais
print(capitales_paises)