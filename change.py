def change():
    expense = 23.75
    money = 100
    vuelto = money - expense
    pesos = int(vuelto)
    centavos = round((vuelto - pesos) * 100)
    print(f'Ingresar gasto:\n{expense}\nDinero recibido\n{money}\n')
    print(f"Vuelto\n")
    print("Pesos:")
    print(pesos)
    print("Centavos:")
    print(centavos)

change()
