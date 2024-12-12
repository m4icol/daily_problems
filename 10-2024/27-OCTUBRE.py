# ---------------------------------------------------------------
# Facil
# Concepto clave: Condicionales
# Descripción: Escribe un programa que pida al usuario un número y determine si es par o impar.
# ---------------------------------------------------------------


print("Verificar si un numero es par o impar")
print("-----------------------------------\n")

num = int(input("Digite un numero: "))

print(f"El número {num} es par." if num % 2 == 0 else f"El número {num} es impar.")


# ---------------------------------------------------------------
# Intermedio
# Concepto clave: Listas y bucles
# Descripción: Crea un programa que tome una lista de nombres y los imprima uno por uno en orden alfabético.
# ---------------------------------------------------------------


nombres = ["Andres", "Manuel", "Gilberto", "Andrew", "Esteban", "Steven"]
print(nombres)

for i in range(1, len(nombres)):
    actual = nombres[i]
    j = i-1

    while j >= 0 and nombres[j] > actual:
        nombres[j+1] = nombres[j]
        j -= 1
    
    nombres[j+1]= actual

print(nombres)


# ---------------------------------------------------------------
# Avanzado
# Concepto clave: Manipulación de cadenas
# Descripción: Escribe una función que reciba una frase y 
# devuelva la misma frase, pero con las palabras en orden inverso.
# ---------------------------------------------------------------

def inversa(texto):
    listaFrase = texto.split()
    listaInversa = []

    for i in range(len(listaFrase) -1, -1, -1):
        listaInversa.append(listaFrase[i])

    listaInversa = " ".join(listaInversa)

    return listaInversa

print(inversa("El dia esta soleado"))