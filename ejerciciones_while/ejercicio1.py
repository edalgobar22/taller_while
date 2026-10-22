"""
ENTRADA
- a
- b

PROCESO
-

SALIDA
-mostrar los enteros que estan dentro del rango sin mostrar los extremos

"""

a = int(input("Ingresa numero entero A: "))
b = int(input("Ingresa numero entero B: "))

while a >= b:
    print("Error, A tiene que ser menor que B.")
    a = int(input("Ingresa numero entero A: "))
    b = int(input("Ingresa numero entero B: "))

if a + 1 == b:
    print("No hay enteros interiores")
else:
    for num in range(a + 1, b):
        print(num)