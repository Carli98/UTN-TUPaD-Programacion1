#Ejercicio 1
edad = int (input ("Ingrese su edad "))
if edad >= 18:
    print("Es mayor de edad")

#Ejercicio 2
nota = int (input("Ingrese su nota "))
if nota >= 6:
    print ("Aprobado")
elif nota < 6:
    print ("Desaprobado")

#Ejercicio 33
numero = int (input("Ingrese un numero: "))
if numero % 2 == 0:
    print ("Ha ingresa un numero par.")
else:
    print ("Ha ingresa un numero impar.")

#Ejercicio 4
edad = int (input("Ingrese su edad: "))
if edad < 12:
    print ("Sos niño/a.")
elif edad >= 12 and edad < 18:
    print ("Sos adolescente.")
elif edad >= 18 and edad < 30:
    print ("Sos adulto/a joven.")
elif edad >= 30:
    print ("Sos adulto/a.")

#ejercicio 5
texto = (input("Ingrese una contraseña entre 8 y 14 caracteres: "))
if (len(texto)) >= 8 and (len(texto)) <= 14:
    print ("Ha ingresa una contraseña correcta")
else:
    print ("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

#Ejercecio 6
import statistics 
import random
numeros_aleatorios = [random.randint(1, 100) for i in range(50)]
media = statistics.mean (numeros_aleatorios)
mediana = statistics.median (numeros_aleatorios)
moda = statistics.mode (numeros_aleatorios)
if media > mediana and mediana > moda:
    sesgo = "positivo"
elif media < mediana and mediana < moda:
    sesgo = "negativo"
else:
    sesgo = "no hay sesgo"
print (f"Media:{media}")
print (f"Mediana:{mediana}")
print (f"Moda:{moda}")
print (f"Resultado:{sesgo}")

#Ejercicio 7
frase = input ("Ingrese una palabra o frase: ")
if frase [-1] in "aeiou":
    print (f"{frase}!")
else:
    print (f"{frase}")

#Ejercicio 8
nombre = input ("Ingrese su nombre: ")
print ("1 para que todo el nombre este en mayusculas.")
print ("2 para que todo el nombre este en minusculas.")
print ("3 para que la primera letra este en mayusculas y las demas en minusculas.")
opcion = input ("Ingrese una opcion: ")
if opcion == "1":
    print (nombre.upper())
elif opcion == "2":
    print (nombre.lower())
elif opcion == "3":
    print (nombre.title())
else:
    print ("Opcion incorrecta.")

#Ejercicio 9
magnitud = float(input("Ingrese la magnitud del terremoto: "))
if magnitud < 3:
    print ("Muy Leve , imperceptible.")
elif magnitud >= 3 and magnitud < 4:
    print ("Leve , ligeramente perceptible.")
elif magnitud >= 4 and magnitud < 5:
    print ("Moderado , sentidos por personar pero no causa daños.")
elif magnitud >= 5 and magnitud < 6:
    print ("Fuerte , puede causar daños en estructuras debiles.")
elif magnitud >= 6 and magnitud < 7:
    print ("Muy fuerte , puede causar daños significativos.")
elif magnitud >= 7:
    print ("Extremo , puede causar grandes daños a gran escala.")

#Ejercicio 10
hemisferio = input ("Ingrese en que hemisferio se encuentra (N/S): ")
mes = int(input("Ingrese que mes es (1-12): "))
dia = int(input("Ingrese que dia del mes es (1-31): "))
if (mes == 12 and dia >=21) or (1<= mes <=2) or (mes == 3 and dia <=20):
    estacion_n = "Invierno"
    estacion_s = "Verano"
elif (mes == 3 and dia >= 21) or (4 <= mes <= 5) or (mes == 6 and dia <=20):
    estacion_n = "Primavera"
    estacion_s = "Otoño"
elif (mes == 6 and dia >=21) or (7 <= mes <= 8) or (mes == 9 and dia <=20):
    estacion_n = "Verano"
    estacion_s = "Invierno"
elif (mes == 9 and dia >=21) or (10 <= mes <= 11) or (mes == 12 and dia <=20):
    estacion_n = "Otoño"
    estacion_s = "Primavera"
if hemisferio == "N":
    print ("Estas en" , estacion_n)
elif hemisferio == "S":
    print ("Estas en" , estacion_s)
else:
    pass
