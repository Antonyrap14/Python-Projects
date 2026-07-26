prodotti = {
    "bici": (1,200)
}

def aggiungi_prodotti(dizionario,nome,quantita,prezzo):
    dizionario[nome] = (quantita,prezzo)

    return dizionario

def rimuovi_prodotto(dizionario,nome):
    if nome in dizionario:
        del dizionario[nome]
    else:
        print("prodotto non presente")
    
    return dizionario

def calcola_totale(prodotti):
    totale = 0
  

    for prodotto,valori in prodotti.items():
        print(f"Prodotto {prodotto} costa {valori[1]}€ e ne hai presi {valori[0]}")
        totale += valori[0] * valori[1]

    print(f"--------------------\nil totale è {totale}")

# MAIN
prodotti = {
    "bici": (1,200)
}

flag = True
while(flag):
    scelta = int(input("1 aggiungi, 2 rimuovi,3 elimina e altri numeri chiudi: "))

    if scelta == 1:
        oggetto = input("inserisci un oggetto: ")
        quantita = int(input("inserisci la quantita: "))
        prezzo = int(input("inserisci il prezzo: "))
        print(aggiungi_prodotti(prodotti,oggetto,quantita,prezzo))
    elif scelta == 2:
        oggetto = input("inserisci oggetto da rimuovere: ")
        print(rimuovi_prodotto(prodotti,oggetto))
    elif scelta == 3:
       calcola_totale(prodotti)
    else:
        print("Grazie per aver usato il programma!")
        flag = False

