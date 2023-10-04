### Estructuras Iterativas
# Ejercicio 1

numeros=[]
for n in range(1500, 2700):
    if n % 7 == 0 and n % 5 == 0:
        numeros.append(n)

print("Los números divisibles por 7 y multiplos de 5 en el rango de 1500 y 2700 son: ")
print(numeros)