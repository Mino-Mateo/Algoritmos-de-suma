import os  # Módulo para limpiar la consola

# Función para limpiar la consola
def limpiar_consola():
    os.system("cls" if os.name == "nt" else "clear")

# Hallar el menor de 2 numeros enteros positivos sin usar 
# condicionales ni operadores ternarios, suponer que los numeros no son iguales
def ejercicio_1():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))

    # Forma 1: Usando resta y multiplicación
    menor = a - (a - b) * ((a - b) > 0)
    print(f"El menor de los dos números es: {menor}")

    # Forma 2: Usando la función min()
    menor_2 = min(a, b)
    print(f"El menor de los dos números usando min() es: {menor_2}")

    # Forma 3: Usando operaciones bit a bit
    menor_3 = (a & ((a - b) >> 31)) + (b & (~((a - b) >> 31)))
    print(f"El menor de los dos números usando operaciones bit a bit es: {menor_3}")

    # Forma 4: Usando la función abs()
    menor_4 = a - abs(a - b) * ((a - b) > 0)
    print(f"El menor de los dos números usando abs() es: {menor_4}")

    # Forma 5: Usando la propiedad de orden en listas
    menor_5 = sorted([a, b])[0]
    print(f"El menor de los dos números usando sorted() es: {menor_5}")

# Hallar si 2 numeros enteros son iguales sin usar operadores de comparación ni de suma o resta
def ejercicio_2():
    a = float(input("Número 1: "))
    b = float(input("Número 2: "))

    # Forma 1: Usando el operador de igualdad
    comparador = a == b
    print(f"Son iguales: {comparador}")

    # Forma 2: Usando la función `abs` para verificar si la diferencia es 0
    comparador_2 = abs(a - b) < 1e-9  # Usamos un pequeño margen de error para números decimales
    print(f"Son iguales usando abs: {comparador_2}")

    # Forma 3: Usando el método `hash` de los números
    comparador_3 = hash(a) == hash(b)
    print(f"Son iguales usando hash: {comparador_3}")

    # Forma 4: Usando la conversión de los números a cadenas
    comparador_4 = str(a) == str(b)
    print(f"Son iguales usando str: {comparador_4}")

    # Forma 5: Usando el operador XOR
    comparador_5 = not (a ^ b)
    print(f"Son iguales usando XOR: {comparador_5}")

# Intercambio de valores sin usar una tercera variable
def ejercicio_3():
    a = 10
    b = 2515

    # Forma 1: Usando la suma y resta (ya utilizada)
    a = a + b  # Ahora 'a' tiene el valor de 'a + b'
    b = a - b  # 'b' obtiene el valor original de 'a'
    a = a - b  # 'a' obtiene el valor original de 'b'
    print(f"Forma 1: a = {a}, b = {b}")

    # Forma 2: Usando el operador XOR (bit a bit)
    a = a ^ b  # 'a' contiene el resultado de 'a' XOR 'b'
    b = a ^ b  # 'b' obtiene el valor original de 'a'
    a = a ^ b  # 'a' obtiene el valor original de 'b'
    print(f"Forma 2: a = {a}, b = {b}")

    # Forma 3: Usando tupla
    a, b = b, a  # Intercambio de valores usando tuplas
    print(f"Forma 3: a = {a}, b = {b}")
    a = 10
    b = 2515
    print(f"a = {a}, b = {b}")

# Sumar sin usar el operador de adición
def ejercicio_4():
    a = 1
    b = 20

    # Forma 1: Usando el operador de resta
    resultado = a - (-b)
    print(f"Forma 1: {resultado}")

    # Forma 2: Usando un bucle (sumar incrementando)
    resultado = a
    for _ in range(b):
        resultado += 1
    print(f"Forma 2: {resultado}")

    # Forma 3: Usando el operador XOR bit a bit (sin la función estándar de suma)
    # Nota: Esto solo es adecuado para números pequeños y no negativos
    while b != 0:
        carry = a & b
        a = a ^ b
        b = carry << 1
    print(f"Forma 3: {a}")

    # Forma 4: Usando la función `sum()` con un rango
    resultado = sum(range(a, a + b))
    print(f"Forma 4: {resultado}")

"""
# Escribe un programa que muestre por consola (con un print) los
# números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
# Múltiplos de 3 por la palabra "fizz".
# Múltiplos de 5 por la palabra "buzz".
# Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""
def ejercicio_5():
    for i in range(1, 101):
        # Forma 1: Usando condicionales estándar
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)

    print("\n--- Otras formas ---\n")

    # Forma 2: Usando un diccionario para simplificar el código
    for i in range(1, 101):
        output = ""
        if i % 3 == 0:
            output += "fizz"
        if i % 5 == 0:
            output += "buzz"
        print(output or i)

    print("\n--- Otras formas ---\n")

    # Forma 3: Usando un operador ternario en la impresión
    for i in range(1, 101):
        print("fizzbuzz" if i % 3 == 0 and i % 5 == 0 else "fizz" if i % 3 == 0 else "buzz" if i % 5 == 0 else i)

    print("\n--- Otras formas ---\n")

    # Forma 4: Usando un generador y el método `join` para optimizar la concatenación
    for i in range(1, 101):
        output = ''.join(['fizz' if i % 3 == 0 else '', 'buzz' if i % 5 == 0 else ''])
        print(output or i)


'''
* Escribe una función que reciba dos palabras (String) y retorne
* verdadero o falso (Bool) según sean o no anagramas.
* - Un Anagrama consiste en formar una palabra reordenando TODAS
*   las letras de otra palabra inicial.
* - NO hace falta comprobar que ambas palabras existan.
* - Dos palabras exactamente iguales no son anagrama.
'''
def ejercicio_6():
    palabra1 = input("Ingresa una palabra: ")
    palabra2 = input("Ingresa otra palabra: ")

    # Convertir las palabras a minúsculas
    palabra1 = palabra1.lower()
    palabra2 = palabra2.lower()

    # Forma 1: Ordenar ambas palabras y compararlas
    if palabra1 == palabra2:
        print("¿Son anagramas?: False")
    else:
        palabra1_ordenada = sorted(palabra1)
        palabra2_ordenada = sorted(palabra2)
        print(f"¿Son anagramas?: {palabra1_ordenada == palabra2_ordenada}")

    print("\n--- Otras formas ---\n")

    # Forma 2: Usar el método `collections.Counter` para contar las ocurrencias de cada letra
    from collections import Counter
    if Counter(palabra1) == Counter(palabra2):
        print(f"¿Son anagramas?: True")
    else:
        print(f"¿Son anagramas?: False")

    print("\n--- Otras formas ---\n")

    # Forma 3: Usar una variable de bandera para comprobar los caracteres
    if len(palabra1) != len(palabra2):  # Si tienen distinta longitud no pueden ser anagramas
        print("¿Son anagramas?: False")
    else:
        es_anagrama = True
        for char in palabra1:
            if palabra1.count(char) != palabra2.count(char):
                es_anagrama = False
                break
        print(f"¿Son anagramas?: {es_anagrama}")

    print("\n--- Otras formas ---\n")

    # Forma 4: Usar un conjunto de letras
    if len(palabra1) != len(palabra2):  # Si tienen distinta longitud no pueden ser anagramas
        print("¿Son anagramas?: False")
    else:
        set1 = set(palabra1)
        set2 = set(palabra2)
        if set1 == set2:
            print(f"¿Son anagramas?: True")
        else:
            print(f"¿Son anagramas?: False")

# Método para verificar si un número es primo
def ejercicio_7():
    num = int(input("Ingresa un número para verificar si es primo: "))
    
    # Forma 1: Método clásico con ciclo for y optimización hasta la raíz cuadrada
    if num <= 1:
        print(f"{num} no es primo.")
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                print(f"{num} no es primo.")
                break
        else:
            print(f"{num} es primo.")

    print("\n--- Otras formas ---\n")

    # Forma 2: Usando un ciclo for sin optimización (menos eficiente)
    if num <= 1:
        print(f"{num} no es primo.")
    else:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} no es primo.")
                break
        else:
            print(f"{num} es primo.")

    print("\n--- Otras formas ---\n")

    # Forma 3: Usando el método `any()` para verificar si hay divisores
    if num <= 1:
        print(f"{num} no es primo.")
    else:
        divisores = any(num % i == 0 for i in range(2, int(num ** 0.5) + 1))
        if divisores:
            print(f"{num} no es primo.")
        else:
            print(f"{num} es primo.")

    print("\n--- Otras formas ---\n")

    # Forma 4: Usando el enfoque recursivo
    def es_primo_recursivo(n, i=2):
        if n <= 1:
            return False
        if i * i > n:
            return True
        if n % i == 0:
            return False
        return es_primo_recursivo(n, i + 1)
    
    if es_primo_recursivo(num):
        print(f"{num} es primo.")
    else:
        print(f"{num} no es primo.")

# Método para invertir una cadena
def ejercicio_8():
    texto = input("Ingresa una cadena para invertir: ")

    # Forma 1: Usando el slicing (rebanado) de Python
    print(f"La cadena invertida es: {texto[::-1]}")

    print("\n--- Otras formas ---\n")

    # Forma 2: Usando el método `reversed()` y `join()`
    print(f"La cadena invertida es: {''.join(reversed(texto))}")

    print("\n--- Otras formas ---\n")

    # Forma 3: Usando un ciclo `for` para invertir la cadena manualmente
    texto_invertido = ""
    for char in texto:
        texto_invertido = char + texto_invertido
    print(f"La cadena invertida es: {texto_invertido}")

    print("\n--- Otras formas ---\n")

    # Forma 4: Usando un ciclo `for` con `append()` en una lista
    lista = []
    for char in texto:
        lista.append(char)
    lista.reverse()  # Invertimos la lista
    print(f"La cadena invertida es: {''.join(lista)}")

# Método para contar la cantidad de ocurrencias de un valor en una lista
def ejercicio_9():
    lista = [1, 2, 3, 4, 5, 1, 2, 1, 3, 1]  # Lista de ejemplo
    valor = int(input("Ingresa un valor para contar sus ocurrencias: "))
    
    # Forma 1: Usando el método `count()` de las listas
    print(f"El valor {valor} aparece {lista.count(valor)} veces en la lista.")

    print("\n--- Otras formas ---\n")

    # Forma 2: Usando un ciclo `for` y un contador manual
    contador = 0
    for item in lista:
        if item == valor:
            contador += 1
    print(f"El valor {valor} aparece {contador} veces en la lista.")

    print("\n--- Otras formas ---\n")

    # Forma 3: Usando `collections.Counter` para contar las ocurrencias
    from collections import Counter
    contador_lista = Counter(lista)
    print(f"El valor {valor} aparece {contador_lista.get(valor, 0)} veces en la lista.")

    print("\n--- Otras formas ---\n")

    # Forma 4: Usando `filter()` y `len()` para contar las ocurrencias
    ocurrencias = len(list(filter(lambda x: x == valor, lista)))
    print(f"El valor {valor} aparece {ocurrencias} veces en la lista.")

# Método para calcular el máximo común divisor (MCD) de dos números
def ejercicio_10():
    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))

    # Forma 1: Usando el algoritmo de Euclides (ya proporcionado)
    # Algoritmo de Euclides
    while b:
        a, b = b, a % b
    print(f"El MCD de los dos números es: {a}")

    print("\n--- Otras formas ---\n")

    # Forma 2: Usando la función `math.gcd()`
    import math
    print(f"El MCD usando `math.gcd()` es: {math.gcd(a, b)}")

    print("\n--- Otras formas ---\n")

    # Forma 3: Usando un ciclo `for` para calcular el MCD manualmente
    def mcd_manual(a, b):
        for i in range(min(a, b), 0, -1):
            if a % i == 0 and b % i == 0:
                return i
        return 1

    print(f"El MCD usando un ciclo `for` es: {mcd_manual(a, b)}")

    print("\n--- Otras formas ---\n")

    # Forma 4: Usando recursión para calcular el MCD
    def mcd_recursivo(a, b):
        if b == 0:
            return a
        return mcd_recursivo(b, a % b)

    print(f"El MCD usando recursión es: {mcd_recursivo(a, b)}")

    a = int(input("Ingresa el primer número: "))
    b = int(input("Ingresa el segundo número: "))

    while b:
        a, b = b, a % b
    print(f"El MCD de los dos números es: {a}")

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