import os  # Módulo para limpiar la consola

# Función para limpiar la consola
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 1: Dado un número entero, calcular la suma de sus divisores.
def ejercicio_1():
    limpiar_consola()
    print("Ejercicio 1: Dado un número entero, calcular la suma de sus divisores.")
    inicio = int(input(f"Introduce un numero entero: "))
    
    # Método 1: Usando un bucle for
    suma = 0
    for i in range(2, inicio):
        if inicio % i == 0:
            suma += i
    print(f"Método 1: La suma de los divisores es: {suma}")
    
    # Método 2: Usando comprensión de lista
    suma = sum([i for i in range(2, inicio) if inicio % i == 0])
    print(f"Método 2: La suma de los divisores es: {suma}")
    
    # Método 3: Usando filter y lambda
    suma = sum(filter(lambda x: inicio % x == 0, range(2, inicio)))
    print(f"Método 3: La suma de los divisores es: {suma}")
    
    input("\nPresiona Enter para continuar...")

# Ejercicio 2: Sumar los elementos únicos de una lista (sin repetir elementos).
def ejercicio_2():
    limpiar_consola()
    print("Ejercicio 2: Sumar los elementos únicos de una lista (sin repetir elementos).")
    lista = [1, 1, 1, 1, 10, 2]
    
    # Método 1: Usando un set para eliminar duplicados
    suma = sum(set(lista))
    print(f"Método 1: La suma de los elementos únicos es igual a: {suma}")
    
    # Método 2: Usando un bucle for y un set manual
    suma = 0
    elementos_unicos = set()
    for i in lista:
        if i not in elementos_unicos:
            suma += i
            elementos_unicos.add(i)
    print(f"Método 2: La suma de los elementos únicos es igual a: {suma}")
    
    # Método 3: Usando comprensión de lista
    suma = sum([i for i in set(lista)])
    print(f"Método 3: La suma de los elementos únicos es igual a: {suma}")
    
    input("\nPresiona Enter para continuar...")

# Ejercicio 3: Calcular la suma de los números que se encuentran entre dos números dados y son divisibles por un tercer número.
def ejercicio_3():
    limpiar_consola()
    print("Ejercicio 3: Calcular la suma de los números que se encuentran entre dos números dados y son divisibles por un tercer número.")
    inicio = int(input(f"Introduce el numero de inicio: "))
    final = int(input(f"Introduce el numero del final: "))
    comparador = int(input(f"Introduce el numero comparador: "))
    
    # Método 1: Usando un bucle for
    suma = 0
    for i in range(inicio, final + 1):
        if i % comparador == 0:
            suma += i
    print(f"Método 1: La suma de los elementos es igual a: {suma}")
    
    # Método 2: Usando comprensión de lista
    suma = sum([i for i in range(inicio, final + 1) if i % comparador == 0])
    print(f"Método 2: La suma de los elementos es igual a: {suma}")
    
    # Método 3: Usando filter y lambda
    suma = sum(filter(lambda x: x % comparador == 0, range(inicio, final + 1)))
    print(f"Método 3: La suma de los elementos es igual a: {suma}")
    
    input("\nPresiona Enter para continuar...")

# Llamar a las funciones
ejercicio_1()
ejercicio_2()
ejercicio_3()