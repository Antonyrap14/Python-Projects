
inventario = {
    "mela": {
        "quantita": 30,
        "prezzo_unitario": 0.50
    },
    "pera": {
        "quantita": 20,
        "prezzo_unitario": 0.30
    },
    "patate": {
        "quantita": 40,
        "prezzo_unitario": 0.70
    }
}

def stampa(dizionario):
    for prodotto,dettagli in dizionario.items():
        print("prodotto :",prodotto)
        print(f"quantita:{dettagli['quantita']}")
        print(f"prezzo:{dettagli['prezzo_unitario']}")
stampa(inventario)

