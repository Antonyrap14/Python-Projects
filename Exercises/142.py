def stampa_positivi(lista):
    positivi = []

    for numero in lista:
        if numero < 0:
            continue
        else:
            positivi.append(numero)

    print("I numeri positivi sono:")
    for elemento in positivi:
        print(elemento)

lista = [1, 2, 3, 4, 5, -1, -2, -3, -4, -5]
stampa_positivi(lista)
