vendite = {
    'mela': 50,
    'banana': 30,
    'arancia': 40
    }

def rimuovi(dizionario,prodotto):

    if prodotto not in dizionario:
        print(f"Non posso rimuovere il prodotto {prodotto}, perchè non presente {dizionario}")

    else:
        dizionario.pop(prodotto)
        print(f"Prodotto rimosso:{prodotto}\nLista prodotti:{vendite}")
    
prodotto = input("inserisci il prodotto:")
rimuovi(vendite,prodotto)