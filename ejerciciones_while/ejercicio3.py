cantidad = 0
suma = 0

while True:
    nota = int(input("Ingrese una nota entre 0 y 100 (-99 para terminar): "))

    if nota == -99:
        break

    if 0 <= nota <= 100:
        suma += nota
        cantidad += 1
    else:
        print("Error, la nota debe estar entre 0 y 100.")

print("Cantidad de notas:", cantidad)

if cantidad > 0:
    promedio = suma / cantidad
    print("Promedio:", promedio)
else:
    print("Sin notas")