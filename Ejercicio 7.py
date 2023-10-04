# Ejercicio 7
n = int(input("Ingrese un numero: "))
a=1
b=0
while a <= n:
	if n % a ==0:
		b=b+1
	a=a+1
if b==2:
	print("El numero",n,"es primo")
else:
	print("El numero",n,"no es primo")