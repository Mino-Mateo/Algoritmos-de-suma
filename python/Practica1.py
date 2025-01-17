import os  # Módulo para limpiar la consola

# Función para limpiar la consola
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")


# Ejercicio 1: Sumar los elementos de una lista dada
def ejercicio_1():
    limpiar_consola()
    print("Ejercicio 1: Sumar los elementos de una lista dada\n")
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Lista: {lista}")

    # Método 1
    suma = sum(lista)
    print(f"Método 1: La suma de todos los elementos es igual a: {suma}")

    # Método 2
    suma = 0
    for i in lista:
        suma += i
    print(f"Método 2: La suma de todos los elementos es igual a: {suma}")

    input("\nPresione Enter para continuar...")

# Ejercicio 2: Sumar todos los números pares en una lista
def ejercicio_2():
    limpiar_consola()
    print("Ejercicio 2: Sumar todos los números pares en una lista\n")
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Lista: {lista}")

    # Método 1: Usando una comprensión de lista
    suma1 = sum([i for i in lista if i % 2 == 0])
    print(f"Método 1: La suma de todos los números pares es igual a: {suma1}")

    # Método 2: Usando un bucle for
    suma2 = 0
    for i in lista:
        if i % 2 == 0:
            suma2 += i
    print(f"Método 2: La suma de todos los números pares es igual a: {suma2}")

    # Método 3: Usando filter y lambda
    suma3 = sum(filter(lambda x: x % 2 == 0, lista))
    print(f"Método 3: La suma de todos los números pares es igual a: {suma3}")

    input("\nPresione Enter para continuar...")

# Ejercicio 3: Sumar todos los números impares en una lista
def ejercicio_3():
    limpiar_consola()
    print("Ejercicio 3: Sumar todos los números impares en una lista\n")
    lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(f"Lista: {lista}")

    # Método 1: Usando una comprensión de lista
    suma1 = sum([i for i in lista if i % 2 != 0])
    print(f"Método 1: La suma de todos los números impares es igual a: {suma1}")

    # Método 2: Usando un bucle for
    suma2 = 0
    for i in lista:
        if i % 2 != 0:
            suma2 += i
    print(f"Método 2: La suma de todos los números impares es igual a: {suma2}")

    # Método 3: Usando filter y lambda
    suma3 = sum(filter(lambda x: x % 2 != 0, lista))
    print(f"Método 3: La suma de todos los números impares es igual a: {suma3}")

    input("\nPresione Enter para continuar...")

# Ejercicio 4: Calcular la suma de los números del 1 al 100
def ejercicio_4():
    limpiar_consola()
    print("Ejercicio 4: Calcular la suma de los números del 1 al 100\n")

    # Método 1: Usando sum() y range
    suma1 = sum(range(1, 101))
    print(f"Método 1: La suma de los números del 1 al 100 es igual a: {suma1}")

    # Método 2: Usando un bucle for
    suma2 = 0
    for i in range(1, 101):
        suma2 += i
    print(f"Método 2: La suma de los números del 1 al 100 es igual a: {suma2}")

    # Método 3: Fórmula matemática
    suma3 = (100 * (100 + 1)) // 2
    print(f"Método 3: La suma de los números del 1 al 100 es igual a: {suma3}")

    input("\nPresione Enter para continuar...")

# Ejercicio 5: Sumar los dígitos de un número entero
def ejercicio_5():
    limpiar_consola()
    print("Ejercicio 5: Sumar los dígitos de un número entero\n")
    numero = 123
    print(f"Número: {numero}")

    # Método 1: Usando sum() y map()
    suma1 = sum(map(int, str(numero)))
    print(f"Método 1: La suma de los dígitos es igual a: {suma1}")

    # Método 2: Usando un bucle for
    suma2 = 0
    for digito in str(numero):
        suma2 += int(digito)
    print(f"Método 2: La suma de los dígitos es igual a: {suma2}")

    # Método 3: Usando una comprensión de lista
    suma3 = sum([int(digito) for digito in str(numero)])
    print(f"Método 3: La suma de los dígitos es igual a: {suma3}")

    input("\nPresione Enter para continuar...")

# Ejercicio 6: Calcular la suma de los números en un rango dado por el usuario
def ejercicio_6():
    limpiar_consola()
    print("Ejercicio 6: Calcular la suma de los números en un rango dado\n")
    inicio = int(input("Ingrese el número de inicio: "))
    fin = int(input("Ingrese el número final: "))

    # Método 1: Usando sum() y range()
    suma1 = sum(range(inicio, fin + 1))
    print(f"Método 1: La suma de los números del {inicio} al {fin} es igual a: {suma1}")

    # Método 2: Usando un bucle for
    suma2 = 0
    for i in range(inicio, fin + 1):
        suma2 += i
    print(f"Método 2: La suma de los números del {inicio} al {fin} es igual a: {suma2}")

    # Método 3: Usando una comprensión de lista
    suma3 = sum([i for i in range(inicio, fin + 1)])
    print(f"Método 3: La suma de los números del {inicio} al {fin} es igual a: {suma3}")

    input("\nPresione Enter para continuar...")

# Ejercicio 7: Sumar números positivos y contar negativos
def ejercicio_7():
    limpiar_consola()
    print("Ejercicio 7: Sumar números positivos y contar negativos\n")
    lista = [0, 1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

    # Método 1: Usando generadores en sum()
    suma_positivos1 = sum(i for i in lista if i > 0)
    count_negativos1 = sum(1 for i in lista if i < 0)
    print(f"Método 1: Suma de positivos: {suma_positivos1}, Negativos: {count_negativos1}")

    # Método 2: Usando un bucle for
    suma_positivos2 = 0
    count_negativos2 = 0
    for i in lista:
        if i > 0:
            suma_positivos2 += i
        elif i < 0:
            count_negativos2 += 1
    print(f"Método 2: Suma de positivos: {suma_positivos2}, Negativos: {count_negativos2}")

    input("\nPresione Enter para continuar...")

# Ejercicio 8: Sumar los números menores a un valor dado
def ejercicio_8():
    limpiar_consola()
    print("Ejercicio 8: Sumar los números menores a un valor dado\n")
    valor = 5
    lista = [0, 1, -2, 3, -4, 5, -6, 7, -8, 9, -10]

    # Método 1: Usando generadores en sum()
    suma1 = sum(i for i in lista if i < valor)
    print(f"Método 1: La suma de los números menores a {valor} es igual a: {suma1}")

    # Método 2: Usando un bucle for
    suma2 = 0
    for i in lista:
        if i < valor:
            suma2 += i
    print(f"Método 2: La suma de los números menores a {valor} es igual a: {suma2}")

    # Método 3: Usando una comprensión de lista
    suma3 = sum([i for i in lista if i < valor])
    print(f"Método 3: La suma de los números menores a {valor} es igual a: {suma3}")

    input("\nPresione Enter para continuar...")

# Ejercicio 9: Pedir al usuario 5 números e imprimir su suma
def ejercicio_9():
    limpiar_consola()
    print("Ejercicio 9: Pedir al usuario 5 números e imprimir su suma\n")

    # Método 1: Usando un bucle for
    suma1 = 0
    for i in range(1, 6):
        numero = int(input(f"Ingrese el número {i}: "))
        suma1 += numero
    print(f"Método 1: La suma de los números ingresados es igual a: {suma1}")

    # Método 2: Usando una lista y sum()
    numeros = [int(input(f"Ingrese el número {i}: ")) for i in range(1, 6)]
    suma2 = sum(numeros)
    print(f"Método 2: La suma de los números ingresados es igual a: {suma2}")

    input("\nPresione Enter para continuar...")

# Ejercicio 10: Sumar números hasta que se introduzca un 0
def ejercicio_10():
    limpiar_consola()
    print("Ejercicio 10: Sumar números hasta que se introduzca un 0\n")

    # Método 1: Usando un bucle while
    suma1 = 0
    while True:
        numero = int(input("Ingrese un número (0 para terminar): "))
        if numero == 0:
            break
        suma1 += numero
    print(f"Método 1: La suma de los números ingresados es igual a: {suma1}")

    # Método 2: Usando una lista y sum()
    print("\nIngrese números uno por uno (0 para terminar):")
    numeros = []
    while True:
        numero = int(input("> "))
        if numero == 0:
            break
        numeros.append(numero)
    suma2 = sum(numeros)
    print(f"Método 2: La suma de los números ingresados es igual a: {suma2}")

    input("\nPresione Enter para continuar...")

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
ejercicio_10()