# Conversión de Números:
# Desarrollen un programa que convierta números decimales a binarios y, de forma opcional, también de binario a decimal.
# Extensión: Validar la entrada y mostrar mensajes de error ante datos incorrectos.


binario = []
operacion = 0
convertido=0
bandera=False

print("Elija una opción: ")

while True:
   
    entrada = input(" 1 - Convertir un número entero en un número binario. \n 2 - Convertir un número binario en un número en base decimal. \n 3 - Salir del programa.\n : ")
    
   
    if entrada == '1' :
            
            binario = []
            bandera = False

            while bandera == False:
                decimal_entrada = input("Ingrese un número entero para convertir en binario: ")
                if decimal_entrada == '':
                    print("Ingrese un número válido...")
                    continue
                if  '.' in decimal_entrada or ',' in decimal_entrada:
                    print("Ingrese un número entero,  no se permite decimal..")
                    continue
                
                bandera=True
                decimal=int(decimal_entrada)

            if decimal < 0 :
                print("El número ingresado es negativo. Ingrese un número positivo")
                continue

            convertido=decimal
            # print(decimal)        
            while decimal >= 1:
                bit = 0
                operacion = decimal // 2
                bit = decimal % 2
                # print(decimal,"dividido 2 " "resto es: ",operacion,"y el reciduo es: ",bit)
                # print("reciduo",bit)
                binario.append(bit)
                decimal=operacion 
            binario_al=[]
            binario_al=binario[::-1]
            print("el número decimal",convertido,"convertido en binario es: ",end="")
            for i in binario_al:
                print(i,end="")
            print("\n")
            bandera = False
            print("Intente nuevamente o elija la opcion 3 para salir")
            print()
          
          
    
    if entrada == '2':
# Pedir al usuario un número binario como cadena
        while True:
# Pedir al usuario un número binario como cadena
            binario = input("Ingrese un número binario: ").strip()
    
            if binario == "":
                print("Entrada inválida. No se permiten espacios vacios")
                continue
            #validar que todos los caracteres sean 0 o 1
            invalido = False
            for bit in binario:
                if bit not in ("0", "1"):
                    print(f"Caracter inválido: {bit}. Solo se permiten los dígitos 0 y 1.")
                    invalido = True
                    break
            if invalido:
                continue
            break

# Convertir la cadena en una lista de dígitos (como caracteres)
        digitos = list(binario)
# Inicializar variables
        potencia = len(digitos) - 1
        decimal = 0

# Recorrer la lista de izquierda a derecha
        for bit in digitos:
            if bit == "1":
                decimal += 2 ** potencia
            potencia -= 1

# Mostrar el resultado

        print("El número ingresado en base decimal es:", decimal)
        print()
        print("Intente nuevamente o elija la opcion 3 para salir")

        continue #vuelve al menu principa

    if entrada == '3':
        break



    

   
