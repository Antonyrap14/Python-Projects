prodotti = {
    100:{
        "prodotto":"pigiama",
        "prezzo": 50,
        "quantita":3
    },
       101:{
        "prodotto":"scarpe",
        "prezzo": 200,
        "quantita":11
    },
       104:{
        "prodotto":"cappello",
        "prezzo": 10,
        "quantita":30
    },
}

def aggiungi(dizionario):
    prodotto = input("inserisci prodotto:")
    quantita = int(input("seleziona quantita:"))
    prezzo = int(input("seleziona prezzo:"))
    codice = int(input("inserisci codice prodotto:"))

    if codice not in dizionario:
        dizionario[codice]  = {
            "prodotto" : prodotto,
            "prezzo" : prezzo,
            "quantita": quantita,
        }
    else:
        aggiorna_quantita(dizionario)

def aggiorna_quantita(dizionario):
    codice = int(input("inserisci il codice"))
    if codice in dizionario:
        quantita = int(input("inserisci quantita:"))
        dizionario[codice]['quantita'] = quantita
    else:
        aggiungi(dizionario)

aggiungi(prodotti)
aggiorna_quantita(prodotti)
print(prodotti)
