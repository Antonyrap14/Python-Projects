# Supponiamo di lavorare per un negozio di elettronica che ha bisogno di processare una lista di ordini dei clienti.
# Ogni ordine è un dizionario che contiene il nome del cliente e una lista di articoli che il cliente ha ordinato.
#  Si desidera saltare l’elaborazione di ogni ordine che contiene un elemento non disponibile. Scrivi una funzione in Python che prende come
#  input una lista di ordini e un set di elementi non disponibili. La funzione dovrebbe stampare il nome del cliente e gli articoli ordinati
#  per ogni ordine che non contiene articoli non disponibili.

ordini_clienti = [
    {
        "paolo":{
            "dentifricio":2,
            "spazzolino":3,
            "colluttorio":3
        },
        "giuseppe":{
            "dentifricio":22,
            "spazzolino":30,
            "colluttorio":31,
            "acqua":2
        }
    }
]

prodotti_indisponibili = ("spazzolino","acqua")

for elementi in ordini_clienti:
    for cliente,ordine in elementi.items():
        print(f"Prodotti del cliente {cliente} processati e disponibili:")
        for oggetto,quantita in ordine.items():
            if oggetto in prodotti_indisponibili:
                continue
            print(f"{oggetto}:{quantita}")

    