# Ejercicio 8

def factorial(num):
    if num < 0:
        return "no definido"
    elif num == 0 or num == 1:
        return 1
    else:
        resultado = 1
        for i in range(2, num + 1):
            resultado *= i
        return resultado

num = int(input("Introduce un número entero no negativo: "))
print("El factorial de", num, "es", factorial(num))