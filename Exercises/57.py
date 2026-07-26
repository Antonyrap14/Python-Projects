articoli = {"pasta","vino"}

def aggiungi(articoli,prodotto):
    articoli.add(prodotto)

while(True):
    scegli = input("vuoi inserire un prodotto?")

    if scegli == "si":
        prodotto = input("inserisci un prodotto")
        aggiungi(articoli,prodotto)
    else:
        print(articoli)
        break
