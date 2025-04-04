def change():
    expense = 23.75
    money = 100
    gasto = float(input("Ingresar gasto:"))
    dinero_recibido = float(input("Dinero recibido"))

    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)

    print("Vuelto")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)
