#Ejercicio 1
notas= [ 5, 2, 6, 7, 9, 8, 4, 6, 4, 7 ]
print (notas)
suma=0
for nota in notas:
    suma += nota
    promedio= suma / len(notas)
print (f"El promedio de las notas es: {promedio}")
nota_alta=notas[0]
nota_baja=notas[0]
for nota in notas:
    if nota > nota_alta:
        nota_alta=nota
    if nota < nota_baja:
        nota_baja=nota
print(f"La nota mas alta es: {nota_alta}")
print(f"La nota mas baja es: {nota_baja}")

#Ejercicio 2
productos= []
for i in range (5):
    producto=input(f"Ingrese el producto {i+1}: ")
    productos.append(producto)
productos_ordenados = sorted(productos)
print("\nLista de productos ordenados alfabeticamente:")
for p in productos_ordenados:
    print (p)
eliminar=input ("\nIngrese el producto que desee eliminar: ")
if eliminar in productos:
    productos.remove(eliminar)
    print(f"\nEl producto {eliminar}, fue eliminado correctamente.")
else:
    print(f"\nEl producto {eliminar}, no se encontro en la lista.")
print("\nLista actualizada de los productos: ")
for p in productos:
    print (p)

#Ejercicio 3
import random
numeros=[]
for i in range(15):
    numeros.append(random.randint(1,100))
print ("Lista de numeros generados: ")
for n in numeros:
    print (n)
pares=[]
impares=[]
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
print("Numeros pares: ")
for p in pares:
    print(p)
print(f"Cantidad de numeros pares:{len (pares)} ")
print("Numeros impares:")
for i in impares:
    print (i)
print (f"Cantidad de numeros impares:{len (impares)} ")

#Ejercicio 4
datos=[1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetir=[]
for elemento in datos:
    if elemento not in sin_repetir:
        sin_repetir.append(elemento)
print ("Lista original: ", datos)
print ("Lista sin repeticiones de datos: ", sin_repetir)

#Ejercicio 5
estudiantes=["Lucia", "Maria", "Carlos", "Julian", "Estefania", "Dario", "Pablo", "Javier"]
print ("Lista de los estudiantes: ")
for e in estudiantes:
    print (e)
opcion = input("\n¿Desea agregar un estudiante (A) o eliminar uno (E)? ").upper()
if opcion == "A":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
    print(f"\nEl estudiante {nuevo} fue agregado correctamente.")
elif opcion == "E":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
        print(f"\nEl estudiante {eliminar} fue eliminado correctamente.")
    else:
        print(f"\nEl estudiante {eliminar} no se encontró en la lista.")
else:
    print("\nOpción no válida. No se realizaron cambios.")
print("\nLista actualizada de los estudiantes:")
for e in estudiantes:
    print(e)

#Ejercicio 6
numeros=[100, 200, 300, 400, 500, 600, 700]
print("Lista de numeros ", numeros)
ultimo=numeros[-1]
for i in range(len(numeros)-1, 0, -1):
    numeros[i]=numeros[i-1]
numeros[0]=ultimo
print ("Lista con rotacion de numero: ", numeros)

#Ejercicio 7
temperaturas = [
    [4, 16],
    [7, 18],
    [5, 22],
    [2, 13],
    [1, 14],
    [3, 25],
    [6, 28], 
    ]
cantidad_filas=len(temperaturas)
cantidad_columna=len(temperaturas[0])
for i in range(cantidad_filas):
    print(temperaturas[i])
suma=0
contador=0
promedio=0
promedio_2=0
for i in temperaturas:
    suma += i[0]
    contador += i[1]
    promedio=suma / len(temperaturas)
    promedio_2=contador / len(temperaturas)
print(f"El promedio de las temperaturas minimas fue de: {promedio}")
print(f"El promedio de las temperaturas maximas fue de: {round(promedio_2, 2)}")
amplitudes = []
for dia in temperaturas:
    amplitudes.append(dia[1] - dia[0])
mayor_amplitud = max(amplitudes)
dia_mayor = amplitudes.index(mayor_amplitud) + 1
print(f"La mayor amplitud térmica fue de {mayor_amplitud}° en el día {dia_mayor}")

#Ejercicio 8
notas=[
    [8, 5, 7],
    [10, 8, 9],
    [8, 9, 6],
    [6, 9, 7],
    [5, 9, 2]
]
cantidad_filas=len(notas)
cantidad_columnas=len(notas[0])
for i in range(cantidad_filas):
    print(notas[i])
print("Promedio de cada estudiante:")
for i in range(len(notas)):
    suma = 0
    for j in range(len(notas[i])):
        suma += notas[i][j]
    promedio = suma / len(notas[i])
    print(f"Estudiante {i+1}: {promedio:.2f}")
materias = len(notas[0])  
for j in range(materias):
    suma = 0
    for i in range(len(notas)):
        suma += notas[i][j]
    promedio = suma / len(notas)
    print(f"Materia {j+1}: {promedio:.2f}")

#Ejercicio 9
tablero = [["-" for _ in range(3)] for _ in range(3)]
def mostrar_tablero():
    for fila in tablero:
        print(" ".join(fila))
    print()
print("Tablero inicial:")
mostrar_tablero()
for turno in range(2):
    if turno % 2 == 0:
        jugador = "X"
    else:
        jugador = "O"
    print(f"Turno del jugador {jugador}")
    fila = int(input("Ingrese la fila (0-2): "))
    columna = int(input("Ingrese la columna (0-2): "))
    if tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador
    else:
        print("Casilla ocupada, pierde el turno")
    mostrar_tablero()

#Ejercicio 10
ventas = [
    [5, 25, 6, 4, 7, 9, 10],  
    [3, 6, 5, 15, 6, 7, 8],    
    [10, 12, 8, 9, 11, 10, 12],
    [4, 5, 1, 7, 8, 18, 5]      
]
print("Total vendido por cada producto:")
totales_productos = []
for i in range(len(ventas)):
    total = sum(ventas[i])  
    totales_productos.append(total)
    print(f"Producto {i+1}: {total}")
totales_dias = []
for j in range (len(ventas[0])): 
    suma_dia = 0
    for i in range(len(ventas)): 
        suma_dia += ventas[i][j]
    totales_dias.append(suma_dia)
dia_max = totales_dias.index(max(totales_dias)) + 1
print(f"El día con mayores ventas fue el día {dia_max} con {max(totales_dias)} ventas.")
producto_max = totales_productos.index(max(totales_productos)) + 1
print(f"El producto más vendido en la semana fue el Producto {producto_max} con {max(totales_productos)} ventas.")
