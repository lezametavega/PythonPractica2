### Métodos de Cadenas

# Ejercicio 9
texto = input("Ingrese una cadena de texto: ")
result = ""

for letra in texto:
    if letra.lower() not in "aeiou":
        result += letra

print("Resultado:", result)