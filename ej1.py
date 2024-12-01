# Función que calcula el porcentaje de un valor
def calcular_porcentaje(valor, porcentaje):
    return valor * porcentaje / 100  # Fórmula para calcular el porcentaje

# Variable para controlar si el usuario desea continuar
continuar = 's'
while continuar == 's':  # El bucle se repite mientras el usuario introduzca 's'
    
    # Solicita el precio al usuario
    precio = float(input("Introduce el precio: "))
    # Solicita el porcentaje de IVA al usuario
    porcentaje_iva = float(input("Introduce el porcentaje de IVA: "))
    
    # Calcula el IVA y el precio sin IVA
    iva = calcular_porcentaje(precio, porcentaje_iva)
    print(f"El IVA es: {iva}")
    print(f"El precio sin IVA es: {precio - iva}")
    
    # Pregunta al usuario si desea calcular otro precio
    continuar = input("¿Quieres calcular otro precio? (s/n): ").lower()
