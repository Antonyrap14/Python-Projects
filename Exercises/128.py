prodotti = [
    {"nome": "Mela", "quantità": 5},
    {"nome": "Banana", "quantità": 8},
    {"nome": "Arancia", "quantità": 3},
    {"nome": "Pera", "quantità": 6},
]

def somma_quantita(prodotti):
    somma = 0

    for elementi in prodotti:
        for chiave,valore in elementi.items():
            if chiave == "quantità":
                somma +=  elementi["quantità"] 
    print(somma)

def somma(prodotti):
    somma = 0
    for prodotto in prodotti:
        somma += prodotto["quantità"]
    print(somma)

    
somma_quantita(prodotti)
somma(prodotti)