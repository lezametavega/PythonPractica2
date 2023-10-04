# Ejercicio 10
meses = {
    "Enero": "01", "Febrero": "02", "Marzo": "03", "Abril": "04",
    "Mayo": "05", "Junio": "06", "Julio": "07", "Agosto": "08",
    "Septiembre": "09", "Octubre": "10", "Noviembre": "11", "Diciembre": "12"
}

fecha = input("Ingresar la fecha en formato mes/día/año: ")

partes = fecha.replace(",", "").split()

if len(partes) == 3 and partes[0] in meses and partes[1].isdigit() and partes[2].isdigit():
    mes = meses[partes[0]]
    dia = partes[1]
    año = partes[2]
    nuevo_formato = f"{año}-{mes}-{dia:02}"
    print(f"Fecha en formato AAAA-MM-DD: {nuevo_formato}")
elif fecha.count("/") == 2:
    mes, dia, año = fecha.split("/")
    nuevo_formato = f"{año}-{mes:02}-{dia:02}"
    print(f"Fecha en formato AAAA-MM-DD: {nuevo_formato}")
else:
    print("Formato no válido. Por favor, ingrese la fecha en el formato solicitado.")