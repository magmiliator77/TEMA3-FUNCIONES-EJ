# Función que cuenta las apariciones de una letra en una frase
def contar_letra(frase, letra):
    # Inicializamos un contador
    contador = 0
    # Recorremos cada carácter de la frase
    for caracter in frase.lower():  # Convertimos la frase a minúsculas para evitar problemas de mayúsculas
        if caracter == letra.lower():  # Comparamos cada carácter con la letra (en minúscula)
            contador += 1  # Incrementamos el contador si hay coincidencia
    return contador  # Devolvemos el número total de apariciones

# Variable para controlar si el usuario desea continuar
continuar = 's'

while continuar == 's':  # El bucle se repite mientras el usuario introduzca 's'
    # Solicita una frase al usuario
    frase = input("Introduce una frase: ")
    # Solicita una letra al usuario
    letra = input("Introduce una letra para buscar en la frase: ")
    
    # Valida que el usuario haya introducido una sola letra
    if len(letra) == 1 and letra.isalpha(): 
        # Verifica que es una letra y tiene longitud 1
        # Cuenta las apariciones de la letra y muestra el resultado
        apariciones = contar_letra(frase, letra)
        print(f"La letra '{letra}' aparece {apariciones} veces en la frase.")
    else:
        print("Error: Debes introducir una única letra válida.")  # Muestra un error si la entrada es inválida
    
    # Pregunta al usuario si desea reiniciar el proceso
    continuar = input("¿Quieres reiniciar el proceso? (s/n): ").lower()
