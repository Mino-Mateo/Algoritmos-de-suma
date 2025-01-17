import os  # Módulo para limpiar la consola

# Función para limpiar la consola
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

# Ejercicio 1: Sumar los elementos de una lista ignorando los números negativos.
def ejercicio_1():
    limpiar_consola()
    print("Ejercicio 1: Sumar los elementos de una lista ignorando los números negativos.")
    lista = [1, 2, 3, -4, 5, -6, 7, 8, 9, 10]
    
    # Método 1: Usando comprensión de listas y la función sum()
    suma = sum(i for i in lista if i > 0)
    print(f"Método 1: La suma de los elementos positivos es igual a: {suma}")

    # Método 2: Usando un bucle for y una condición
    suma = 0
    for i in lista:
        if i > 0:
            suma += i
    print(f"Método 2: La suma de los elementos positivos es igual a: {suma}")

    # Método 3: Usando filter() y sum()
    suma = sum(filter(lambda x: x > 0, lista))
    print(f"Método 3: La suma de los elementos positivos es igual a: {suma}")

    # Método 4: Usando un bucle for con una lista temporal
    suma = 0
    positivos = [i for i in lista if i > 0]
    for i in positivos:
        suma += i
    print(f"Método 4: La suma de los elementos positivos es igual a: {suma}")

    input("\nPresiona Enter para continuar...")

# Ejercicio 2: Suma de los cuadrados de los números del 1 al 10.
def ejercicio_2():
    limpiar_consola()
    print("Ejercicio 2: Suma de los cuadrados de los números del 1 al 10.")
    
    # Método 1: Usando comprensión de listas y la función sum()
    suma = sum(i**2 for i in range(1, 11))
    print(f"Método 1: La suma de los cuadrados es igual a: {suma}")

    # Método 2: Usando un bucle for
    suma = 0
    for i in range(1, 11):
        suma += i**2
    print(f"Método 2: La suma de los cuadrados es igual a: {suma}")

    # Método 3: Usando map() con lambda
    suma = sum(map(lambda x: x**2, range(1, 11)))
    print(f"Método 3: La suma de los cuadrados es igual a: {suma}")

    # Método 4: Usando una lista temporal
    cuadrados = [i**2 for i in range(1, 11)]
    suma = sum(cuadrados)
    print(f"Método 4: La suma de los cuadrados es igual a: {suma}")

    input("\nPresiona Enter para continuar...")

# Ejercicio 3: Sumar números del 1 hasta un número dado.
def ejercicio_3():
    limpiar_consola()
    print("Ejercicio 3: Sumar números del 1 hasta un número dado.")
    num = int(input("Ingrese un número entero: "))
    
    # Método 1: Usando sum() con range()
    suma = sum(range(1, num + 1))
    print(f"Método 1: La suma de los números del 1 al {num} es igual a: {suma}")

    # Método 2: Usando un bucle for
    suma = 0
    for i in range(1, num + 1):
        suma += i
    print(f"Método 2: La suma de los números del 1 al {num} es igual a: {suma}")

    # Método 3: Usando la fórmula de la suma de una progresión aritmética
    suma = num * (num + 1) // 2
    print(f"Método 3: La suma de los números del 1 al {num} es igual a: {suma}")

    # Método 4: Usando reduce() de functools
    from functools import reduce
    suma = reduce(lambda x, y: x + y, range(1, num + 1))
    print(f"Método 4: La suma de los números del 1 al {num} es igual a: {suma}")

    input("\nPresiona Enter para continuar...")

# Ejercicio 4: Sumar elementos en posiciones pares de una lista.
def ejercicio_4():
    limpiar_consola()
    print("Ejercicio 4: Sumar elementos en posiciones pares de una lista.")
    lista = [10, 1, 10, 1, 10, 1, 10, 1, 10, 1]
    
    # Método 1: Usando comprensión de listas y sum()
    suma = sum(lista[i] for i in range(len(lista)) if i % 2 == 0)
    print(f"Método 1: La suma de los elementos en posiciones pares es igual a: {suma}")

    # Método 2: Usando un bucle for
    suma = 0
    for i in range(len(lista)):
        if i % 2 == 0:
            suma += lista[i]
    print(f"Método 2: La suma de los elementos en posiciones pares es igual a: {suma}")

    # Método 3: Usando slice
    suma = sum(lista[::2])
    print(f"Método 3: La suma de los elementos en posiciones pares es igual a: {suma}")

    # Método 4: Usando un filtro con filter()
    suma = sum(filter(lambda x: x % 2 == 0, [lista[i] for i in range(len(lista))]))
    print(f"Método 4: La suma de los elementos en posiciones pares es igual a: {suma}")

    input("\nPresiona Enter para continuar...")

# Ejercicio 5: Sumar los múltiplos de 3 en un rango.
def ejercicio_5():
    limpiar_consola()
    print("Ejercicio 5: Sumar los múltiplos de 3 en un rango.")
    inicio = int(input("Introduce un valor inicial: "))
    final = int(input("Introduce un valor final: "))
    
    # Método 1: Usando comprensión de listas y sum()
    suma = sum(i for i in range(inicio, final + 1) if i % 3 == 0)
    print(f"Método 1: La suma de los múltiplos de 3 es igual a: {suma}")

    # Método 2: Usando un bucle for
    suma = 0
    for i in range(inicio, final + 1):
        if i % 3 == 0:
            suma += i
    print(f"Método 2: La suma de los múltiplos de 3 es igual a: {suma}")

    # Método 3: Usando un filtro con filter()
    suma = sum(filter(lambda x: x % 3 == 0, range(inicio, final + 1)))
    print(f"Método 3: La suma de los múltiplos de 3 es igual a: {suma}")

    # Método 4: Usando un bucle for con step
    suma = sum(range(inicio, final + 1, 3))
    print(f"Método 4: La suma de los múltiplos de 3 es igual a: {suma}")

    input("\nPresiona Enter para continuar...")

# Ejercicio 6: Sumar números en una lista hasta encontrar un negativo.
def ejercicio_6():
    limpiar_consola()
    print("Ejercicio 6: Sumar números en una lista hasta encontrar un negativo.")
    lista = [1, 2, -10, 4, 5, 6, 7, -8, 9, 10]
    
    # Método 1: Usando un bucle for con break
    suma = 0
    for i in lista:
        if i < 0:
            break
        suma += i
    print(f"Método 1: La suma total es igual a: {suma}")
    
    # Método 2: Usando un generador con next()
    suma = 0
    for i in iter(lista):
        if i < 0:
            break
        suma += i
    print(f"Método 2: La suma total es igual a: {suma}")
    
    # Método 3: Usando un filtro con filter()
    suma = sum(list(filter(lambda x: x >= 0, lista)))
    print(f"Método 3: La suma total es igual a: {suma}")
    
    # Método 4: Usando while con una condición manual
    suma = 0
    index = 0
    while index < len(lista) and lista[index] >= 0:
        suma += lista[index]
        index += 1
    print(f"Método 4: La suma total es igual a: {suma}")
    
    input("\nPresiona Enter para continuar...")

# Ejercicio 7: Sumar elementos de una matriz.
def ejercicio_7():
    limpiar_consola()
    print("Ejercicio 7: Sumar elementos de una matriz.")
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    
    # Método 1: Usando sum() y comprensión de listas
    suma = sum(sum(fila) for fila in matriz)
    print(f"Método 1: La suma de todos los elementos de la matriz es igual a: {suma}")
    
    # Método 2: Usando un bucle for anidado
    suma = 0
    for fila in matriz:
        for i in fila:
            suma += i
    print(f"Método 2: La suma de todos los elementos de la matriz es igual a: {suma}")
    
    # Método 3: Usando la función reduce()
    from functools import reduce
    suma = reduce(lambda x, y: x + y, [sum(fila) for fila in matriz])
    print(f"Método 3: La suma de todos los elementos de la matriz es igual a: {suma}")
    
    # Método 4: Usando un generador y la función sum()
    suma = sum(i for fila in matriz for i in fila)
    print(f"Método 4: La suma de todos los elementos de la matriz es igual a: {suma}")
    
    input("\nPresiona Enter para continuar...")

# Ejercicio 8: Sumar números primos en un rango.
def ejercicio_8():
    limpiar_consola()
    print("Ejercicio 8: Sumar números primos en un rango.")
    inicio = int(input("Ingrese el número de inicio mayor a 1: "))
    final = int(input("Ingrese el número final: "))
    
    # Método 1: Usando un bucle for con la verificación de números primos
    suma = 0
    for i in range(inicio, final + 1):
        if i > 1 and all(i % j != 0 for j in range(2, int(i**0.5) + 1)):
            suma += i
    print(f"Método 1: La suma de los números primos en el rango es igual a: {suma}")
    
    # Método 2: Usando una función separada para verificar si un número es primo
    def es_primo(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
    
    suma = 0
    for i in range(inicio, final + 1):
        if es_primo(i):
            suma += i
    print(f"Método 2: La suma de los números primos en el rango es igual a: {suma}")
    
    # Método 3: Usando un filtro con filter() para los primos
    suma = sum(filter(lambda x: x > 1 and all(x % j != 0 for j in range(2, int(x**0.5) + 1)), range(inicio, final + 1)))
    print(f"Método 3: La suma de los números primos en el rango es igual a: {suma}")
    
    input("\nPresiona Enter para continuar...")

# Ejercicio 9: Calcular la suma de una lista ingresada por el usuario.
def ejercicio_9():
    limpiar_consola()
    print("Ejercicio 9: Calcular la suma de una lista ingresada por el usuario.")
    lista = input("Ingrese una lista de números separados por comas: ")
    
    # Método 1: Usando sum() con comprensión de lista
    suma = sum(int(i) for i in lista.split(","))
    print(f"Método 1: La suma de los números ingresados es igual a: {suma}")
    
    # Método 2: Usando un bucle for
    suma = 0
    for i in lista.split(","):
        suma += int(i)
    print(f"Método 2: La suma de los números ingresados es igual a: {suma}")
    
    # Método 3: Usando map() para convertir los elementos a enteros y sumarlos
    suma = sum(map(int, lista.split(",")))
    print(f"Método 3: La suma de los números ingresados es igual a: {suma}")
    
    # Método 4: Usando reduce()
    from functools import reduce
    suma = reduce(lambda x, y: x + y, map(int, lista.split(",")))
    print(f"Método 4: La suma de los números ingresados es igual a: {suma}")
    
    input("\nPresiona Enter para continuar...")

# Llamar a las funciones
ejercicio_1()
ejercicio_2()
ejercicio_3()
ejercicio_4()
ejercicio_5()
ejercicio_6()
ejercicio_7()
ejercicio_8()
ejercicio_9()