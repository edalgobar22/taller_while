while True:
    c = float(input("Ingrese el capital inicial: "))
    i = float(input("Ingrese la tasa de interés anual (%): "))
    m = int(input("Ingrese la cantidad de años: "))

    if c >= 0 and 0 < i < 100 and m > 0:
        break
    else:
        print("Datos inválidos, ingrese nuevamente los tres valores.")

saldo = c

for año in range(1, m + 1):
    interes = saldo * i / 100
    saldo = saldo + interes

    print("Saldo al finalizar el año", año, ":", round(saldo, 2))

print("Saldo final:", round(saldo, 2))