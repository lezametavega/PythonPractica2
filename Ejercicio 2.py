# Ejercicio 2

n_filas = 5

for i in range(1, n_filas * 2):
    if i <= n_filas:
        print("* " * i)
    else:
        print("* " * (n_filas * 2 - i))