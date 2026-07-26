prodotti = {
    "laptop": {"quantità": 5, "prezzo": 1000},
    "smartphone": {"quantità": 15, "prezzo": 500},
    "tablet": {"quantità": 20, "prezzo": 300},
    "monitor": {"quantità": 7, "prezzo": 150}
}

def dictionary(prodotti):
    return {
        prodotto:{
            "quantità": dettagli["quantità"],
            "prezzo":dettagli["prezzo"]*0.8
        }
        for prodotto,dettagli in prodotti.items()
        if dettagli["quantità"] > 10 
    }

print(dictionary(prodotti))