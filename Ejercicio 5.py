### Funciones

# Ejercicio 5
def cantidad_digitos(numero, digito):
   
    cantidad = str(numero).count(str(digito))
    return cantidad

numero = int(input("Ingrese un número entero: "))
digito = int(input("Ingrese un dígito para contar: "))

cantidad = cantidad_digitos(numero, digito)
print(f"Cantidad de veces {digito} en el número: {cantidad}.")