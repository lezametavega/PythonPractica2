# Ejercicio 4

alumnos = []

n = int(input("Ingresar la cantidad de alumnos: "))

for _ in range(n):
    
    nombre = input("Ingresar el nombre del alumno: ")

    calificaciones = []
    for i in range(32):
        calificacion = float(input(f"Ingrese la calificación {i + 1} para {nombre}: "))
        calificaciones.append(calificacion)

    alumno = {"Alumno": nombre, "Notas": calificaciones}
    alumnos.append(alumno)

print("\nListado de Alumnos:")
for alumno in alumnos:
    print(f"Alumno: {alumno['Alumno']}, Calificaciones: {alumno['Notas']}")