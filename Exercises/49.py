prodotti = {
    "pc":200,
    "tablet" : 1000,
    "monitor":150,
    "orologi":122
}

def rimuovi(dizionario,prodotto):
    if prodotto in dizionario:
        dizionario.pop(prodotto)
        return dizionario,"\n Il prodotto eliminato è",prodotto
    else:
        return "Il prodotto non è già presente"

#################################################
prodotto = input("Inserisci prodotto da rimuovere:")
print(rimuovi(prodotti,prodotto))