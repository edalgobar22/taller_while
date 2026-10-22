cantidad = 0

while True:
    salario_mensual = float(input("Ingrese el salario mensual: "))

    if salario_mensual == 0:
        break

    if salario_mensual > 0:
        dias = int(input("Ingrese los días trabajados: "))
        bonos = float(input("Ingrese los bonos: "))
        deducciones = float(input("Ingrese otras deducciones: "))

        salario_proporcional = salario_mensual * dias / 30
        devengado = salario_proporcional + bonos
        neto = devengado * 0.83 - deducciones

        cantidad += 1

        print("Pago neto del trabajador:", neto)

if cantidad == 0:
    print("Sin trabajadores")