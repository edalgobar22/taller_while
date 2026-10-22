"""
ENTRADA

PROCESO
- 

SALIDA
- sumar todos los digitos de la lectura, haste que aparezsca el primer -50, si el primero numero es -50 la lectura es 0
"""

centinela = -50
num = 0
total = 0


while True:
    num = int(input("Ingrese un numero: "))
    if num == centinela:
        break
    total += num

print("suma: ", total)


    
    
    


