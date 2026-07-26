negozio = {
    "pasta":1,
    "vino":20,
    "acqua":30,
    "pane":55
}

def aggiungi(negozio,prodotto,quantita):
    if prodotto not in negozio:
        negozio[prodotto] = quantita
        return negozio
    else:
        return "{0} già presente nel negozio".format(prodotto)

def aggiorna(negozio,prodotto,quantita):
    if prodotto in negozio:
        negozio[prodotto] = quantita
        return "{0} il prodotto è stato aggiornato con la quantita {1}".format(prodotto,quantita),f"\n{negozio}"
    else:
        return "{0} non è presente nel negozio".format(prodotto)

def quantita_articoli(negozio,prodotto):
    for elemento,quantita in negozio.items():
        if elemento == prodotto:
            return f"{prodotto}:{quantita}"
    

#MAIN
flag = True
while(flag):
    scegli = int(input("vuoi aggiornare 1, aggiungere 2 oppure vedere la quantta di un pordotto 3, altrimenti schiaccia un tasto per uscire"))

    if scegli == 1:
        prodotto = input("inserisci il nome del prodotto:")
        quantita = int(input("inserisci le quantita: "))
        print(aggiorna(negozio,prodotto,quantita))
    elif scegli == 2:
        prodotto = input("inserisci il nome del prodotto:")
        quantita = int(input("inserisci le quantita: "))
        print(aggiungi(negozio,prodotto,quantita))
    elif scegli == 3:
        prodotto = input("inserisci prodotto:")
        print(quantita_articoli(negozio,prodotto))
    else:
        print("Chiusura del programma....")
        flag = False

