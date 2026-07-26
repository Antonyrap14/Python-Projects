def inserisci_prezzo():
    totale = 0

    while(True):
        prezzo = int(input("inserisci prezzo:"))

        if prezzo < 0:
            continue
        
        if prezzo == 0:
            print("Il totale è {0}".format(totale))
            break

        totale += prezzo

inserisci_prezzo()