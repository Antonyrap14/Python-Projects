inventario = {
    "pizza":3,
    "pasta":24,
    "salame":12
}

def aggiungi_prodotti(dizionario):
    while(True):
        scegli = input("vuoi aggiungere un prodotto?")
        scelta = scegli.capitalize()
        if scelta == "Si":
            nome = input("inserisci un nome:")
            quantita = input("inserisci quantita:")
            inventario[f"{nome}"] = quantita
        else:
            print("va bene...ti mostro gli oggetti")
            print(inventario)
            break
    
aggiungi_prodotti(inventario)