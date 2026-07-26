spesa = {}

def inserisci(spesa):
    while(True):
        prodotto = input("inserisci prodotto:")
        prezzo = float(input("inserisci prezzo"))
        if prezzo == 0:
            break
        else:
            spesa[prodotto] = prezzo

def prezzo(spesa):
    totale = 0

    for prezzo in spesa.values():
        totale += prezzo
    
    for prodotto,prezzo in spesa.items():
        print("{0} {1}".format(prodotto,prezzo))
    
    print("Ciao cliente, hai speso {0}".format(totale))
# MAIN
inserisci(spesa)
prezzo(spesa)



    


