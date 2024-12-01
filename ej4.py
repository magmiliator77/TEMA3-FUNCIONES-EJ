# Función que verifica si un número es primo
def es_primo(numero):
    if numero <= 1:  # Los números menores o iguales a 1 no son primos
        return False
    
    # Bucle para verificar si el número tiene divisores distintos de 1 y de sí mismo
    for i in range(2, int(numero ** 0.5) + 1):  # Comprueba hasta la raíz cuadrada del número
        if numero % i == 0:  # Si hay un divisor, no es primo
            return False
    return True  # Si no se encontró ningún divisor, el número es primo

# Variable para controlar si el usuario desea continuar
continuar = 's'
while continuar == 's':  # El bucle se repite mientras el usuario introduzca 's'
    # Solicita un número al usuario

    numero = int(input("Introduce un número: "))
    # Verifica si el número es primo y muestra el resultado


    
    if es_primo(numero):
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")
    
    # Pregunta al usuario si desea comprobar otro número
    continuar = input("¿Quieres comprobar otro número? (s/n): ").lower()
