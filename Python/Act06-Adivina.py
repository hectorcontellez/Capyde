from random import randint
# Solicita el Nombre
nombre = input("Escribe tu nombre: ")

# Genera el Número Aleatorio
numero_aleatorio = randint(1,100)
# print(numero_aleatorio)

# Inicia el contador de intentos
intento = 1

# Inicia el Ciclo de 8 Intentos
while intento < 9:
    # Escribe el número de Intento
    print("Intento No. ", intento)
    # Se solicitael número
    numero = int(input("Escribe un número del 1 al 100: "))
    # Se revisa si el valor esta dentro del Rango
    if numero > 0 and numero < 101:
        # Condición ganadora 
        if numero == numero_aleatorio:
            print("Felicidades", nombre, "adivinaste al intento:", intento)
            print("""
     ___                   _       
    / __|__ _ _ _  __ _ __| |_ ___ 
   | (_ / _` | ' \/ _` (_-<  _/ -_)
    \___\__,_|_||_\__,_/__/\__\___|
                    """)
            break
        # Condicion si el numero es menor
        elif numero < numero_aleatorio:
            print("-----------------------------------------------------------------------------")
            print("[-] Valor Incorrecto --> Pista: El número: ", numero," es menor al correcto")
            print("-----------------------------------------------------------------------------")
        # Condicion si el numero es mayor
        elif numero > numero_aleatorio:
            print("-----------------------------------------------------------------------------")
            print("[-] Valor Incorrecto --> Pista: El número: ", numero," es mayor al correcto")
            print("-----------------------------------------------------------------------------")
    else:
        # Mensaje informando que el valor no es correcto
        print("El valor ingresado: ", numero," no es el solicitado")
    intento +=1
# Muestra el número aleatorio
print("El numero es: ",numero_aleatorio)
