def calcola_totale(prodotti):
    totale = 0

    if len(prodotti) == 0:
        print("non ci sono prodotti")
    else:
        for prezzo,quantita in prodotti:
            new_prezzo = prezzo * quantita
            totale += new_prezzo
        print(totale)
#MAIN
prodotti = [
    (3.5,2),
    (2,5),
    (10,1),
    (1.5,3)
]
prod = []
calcola_totale(prodotti)
calcola_totale(prod)