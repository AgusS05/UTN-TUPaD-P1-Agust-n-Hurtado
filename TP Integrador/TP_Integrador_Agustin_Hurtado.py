# Declaración de funciones
def crear_arbol(valor):
    return [valor, [], []]

def insertar_izquierda(nodo, nuevo_valor):
    subarbol_izq = nodo[1]
    if subarbol_izq:
        nodo[1] = [nuevo_valor, subarbol_izq, []]
    else:
        nodo[1] = [nuevo_valor, [], []]

def insertar_derecha(nodo, nuevo_valor):
    subarbol_der = nodo[2]
    if subarbol_der:
        nodo[2] = [nuevo_valor, [], subarbol_der]
    else:
        nodo[2] = [nuevo_valor, [], []]

def imprimir_arbol_rotado(arbol, nivel=0):
    if arbol:
        imprimir_arbol_rotado(arbol[2], nivel + 1)
        print('   ' * nivel + str(arbol[0]))
        imprimir_arbol_rotado(arbol[1], nivel + 1)

def es_hoja(nodo):
    return nodo[1] == [] and nodo[2] == []

def listar_hojas(arbol, hojas=None):
    if hojas is None:
        hojas = []
    if arbol:
        if es_hoja(arbol):
            hojas.append(arbol[0])
        else:
            listar_hojas(arbol[1], hojas)
            listar_hojas(arbol[2], hojas)
    return hojas

# Recorrido preorden
def recorrido_preorden(arbol):
    if arbol:
        print(arbol[0], end=' ')
        recorrido_preorden(arbol[1])
        recorrido_preorden(arbol[2])

# Recorrido inorden
def recorrido_inorden(arbol):
    if arbol:
        recorrido_inorden(arbol[1])
        print(arbol[0], end=' ')
        recorrido_inorden(arbol[2])

# Recorrido postorden
def recorrido_postorden(arbol):
    if arbol:
        recorrido_postorden(arbol[1])
        recorrido_postorden(arbol[2])
        print(arbol[0], end=' ')

# Crear jerarquía de proceso de atención al cliente
proceso = crear_arbol("Inicio de Atención")

# Primer nivel
insertar_izquierda(proceso, "Recepción de Solicitud")
insertar_derecha(proceso, "Cierre de Caso")

# Segundo nivel - Recepción
insertar_izquierda(proceso[1], "Identificación del Cliente")
insertar_derecha(proceso[1], "Registro de Solicitud")

# Segundo nivel - Cierre
insertar_izquierda(proceso[2], "Encuesta de Satisfacción")
insertar_derecha(proceso[2], "Archivo de Caso")

# Tercer nivel - Recepción
insertar_izquierda(proceso[1][1], "Verificación de Datos")
insertar_derecha(proceso[1][2], "Asignación a Responsable")

# Tercer nivel - Cierre
insertar_izquierda(proceso[2][1], "Análisis de Resultados")
insertar_derecha(proceso[2][2], "Notificación al Cliente")

# Imprimir jerarquía rotada
print("Estructura del proceso de atención al cliente (vista rotada 90°):")
imprimir_arbol_rotado(proceso)

print("\nEtapas finales del proceso (nodos hoja):")
print(", ".join(listar_hojas(proceso)))

# Mostrar recorrido preorden
print("\nRecorrido preorden: raíz - izquierda - derecha")
recorrido_preorden(proceso)

# Mostrar recorrido inorden
print("\nRecorrido inorden: izquierda - raíz - derecha")
recorrido_inorden(proceso)

# Mostrar recorrido postorden
print("\nRecorrido postorden: izquierda - derecha - raíz")
recorrido_postorden(proceso)