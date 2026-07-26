prezzi = [19.99, 29.99, 4.99, 2.49, 49.99]

def calcolo_iva(lista):
    iva = 0.22
    new_lista = [
        round(((prezzo * 0.22) + prezzo),2)
        for prezzo in prezzi
    ]
    print(new_lista)

calcolo_iva(prezzi)