import time

def generar_iterativo(semilla_inicial, a, c, m):
    semilla_actual = semilla_inicial
    resultados = []
    valores_vistos = set()  # Usamos un conjunto para almacenar los números generados
    iteracion = 0

    while True:
        # Generamos el siguiente número
        nuevo_numero = (a * semilla_actual + c) % m
        
        # Verificamos si el número ya ha sido generado antes
        if nuevo_numero in valores_vistos:
            value = valor
            break
        
        # Agregamos el nuevo número al conjunto y a la lista de resultados
        valores_vistos.add(nuevo_numero)
        
        valor = add([iteracion,semilla,nuevo_numero,nuevo_numero/m])
        
        resultados.append(nuevo_numero)
        
        # Imprimimos el número generado
        print(nuevo_numero)
        
        # Actualizamos la semilla actual
        semilla_actual = nuevo_numero
        iteracion += 1
        
    return resultados

def main():
    semilla_input = input("Ingresa la semilla o presiona enter para usar la hora del sistema: ")

    # Verificamos si el usuario ingresó una semilla
    if semilla_input.strip():
        semilla_inicial = int(semilla_input)
    else:
        semilla_inicial = int(time.time())  # Usamos la hora del sistema como semilla

    # Parámetros del generador congruencial lineal
    a = 5  # Multiplicador
    c = 1  # Incremento
    m = 9  # Módulo
    
    # Iniciamos la generación de números iterativamente
    print(f"Semilla inicial: {semilla_inicial}")
    resultados = generar_iterativo(semilla_inicial, a, c, m)
    print(f"Resultados: {resultados}")

if __name__ == "__main__":
    main()
