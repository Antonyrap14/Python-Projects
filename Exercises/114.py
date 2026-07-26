numero_giorni = int(input("Numero giorni noleggio:"))

def prezzo(numero_giorni):
    prezzo = 0
    prezzo_totale = 0

    if numero_giorni <= 30:
        print(f"il prezzo è di 5 euro")
    else:
        for giorno in range(30,numero_giorni):
            prezzo += 2
        prezzo_totale = prezzo + 5
        print(f"Il totale è {prezzo_totale}")

prezzo(numero_giorni)
