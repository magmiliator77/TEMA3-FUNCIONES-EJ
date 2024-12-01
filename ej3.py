# Función que calcula la media de una lista de números
def calcular_media(numeros):
    return sum(numeros) / len(numeros)  # Suma los números y divide entre la cantidad de elementos

# Variable para controlar si el usuario desea continuar
continuar = 's'
while continuar == 's':  # El bucle se repite mientras el usuario introduzca 's'
    numeros = []  # Lista vacía para almacenar los números
    print("Introduce 10 números entre 1 y 50:")
    
    # Bucle para solicitar 10 números al usuario
    for i in range(10):
        numero = int(input(f"Introduce el número {i+1}: "))  # Solicita un número
        
        # Verifica que el número esté en el rango válido

        while numero < 1 or numero > 50:
            print("El número debe estar entre 1 y 50.")  # Muestra un mensaje de error si el número no es válido
            numero = int(input(f"Introduce el número {i+1}: "))  # Solicita nuevamente el número
        numeros.append(numero)  # Agrega el número válido a la lista
    
    # Calcula la media y muestra el resultado
    media = calcular_media(numeros)
    print(f"La media de los números introducidos es: {media}")

    # Pregunta al usuario si desea reiniciar el proceso
    continuar = input("¿Quieres iniciar el proceso de nuevo? (s/n): ").lower()
