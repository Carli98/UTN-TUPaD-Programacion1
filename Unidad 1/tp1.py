#ejercicio 1
print ("hola mundo")

#ejercicio 2
nombre =  input("Por favor ingrese su nombre ")
print ("Hola" , nombre , "!" )

#ejercicio 3
nombre = input ("Por favor ingrese su nombre: ")
apellido = input ("Ingrese su apellido: ")
edad = input ("Ingrese su edad: ")
residencia = input ("Ingrese su residencia: ")
print(f"Soy {nombre} {apellido} , tengo {edad} años y vivo en {residencia}.")

#ejercicio 4
import math
radio = float(input("Por favor ingresa el radio de un circulo: "))
area_circulo = math.pi*(radio)**2
perimetro_circulo = 2*math.pi*radio
print (f"El Area del circulo es {area_circulo} y el Perimetro es {perimetro_circulo}.")

#ejercicio 5
cant_segundo = float(input("Por favor ingrese la cantidad de segundos que desa convertir: "))
cant_horas = round(cant_segundo/3600, 2)
print (f"El equivalente a {cant_segundo} segundos son {cant_horas} horas.")

#ejercicio 6
numero = int(input("Por favor ingrese un numero entero: "))
print (f"""
       {numero}*0 = {numero*0}
       {numero}*1 = {numero*1}
       {numero}*2 = {numero*2}
       {numero}*3 = {numero*3}
       {numero}*4 = {numero*4}
       {numero}*5 = {numero*5}
       {numero}*6 = {numero*6}
       {numero}*7 = {numero*7}
       {numero}*8 = {numero*8}
       {numero}*9 = {numero*9}
       {numero}*10 = {numero*10}
       """)

#ejercicio 7
num1 = int(input("Por favor ingrese un numero entero mayor que 0: "))
num2 = int(input("Por favor ingrese otro numero entero mayor que 0: "))
suma= num1+num2
div= num1/num2
mult= num1*num2
resta= num1-num2
print (f"""
       resultado de la suma: {suma}
       resultado de la division: {div}
       resultado de la multiplicacion:{mult}
       resultado de la resta: {resta}
       """)

#ejercicio 8
peso = float(input("Por favor ingrese su peso: "))
altura = float(input("Por favor ingrese su altura: "))
imc= round(peso/altura**2, 2)
print (f"Su indice de masa corporal es de {imc}.")

#ejercicio 9
temp = float(input("Por favor ingrese una temperatura en grados celcius: "))
grado_f = round((9/5)*temp+32, 2)
print (f"La temperatura en Grados Fahrenheit es de {grado_f}.")

#ejercicio 10
num1 = float(input("Por favor ingrese un numero: "))
num2 = float(input("Por favor ingrese un numero: "))
num3 = float(input("Por favor ingrese un numero: "))
promedio = round((num1+num2+num3)/3, 2)
print (f"El promedio de los numeros ingresado es: {promedio}.")