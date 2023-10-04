# Ejercicio 3
numeros = []
num_pares = 0
num_impares = 0

while True:
    ingresar = input("¿Desea ingresar un número? (SI/NO): ")
    if ingresar.upper() == "SI":
        try:
            numero = int(input("Ingrese el número: "))
            numeros.append(numero)
            if numero % 2 == 0:
                num_pares += 1
            else:
                num_impares += 1
        except ValueError:
            print("Por favor, ingrese un número válido.")
    elif ingresar.upper() == "NO":
        break
    else:
        print("Respuesta no válida. Responda con SI o NO.")

print("Números ingresados:", numeros)
print("Cantidad de números pares:", num_pares)
print("Cantidad de números impares:", num_impares)