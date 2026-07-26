# Supponiamo di avere una lista di prodotti venduti in un negozio di elettronica durante una settimana.
#  prodotti_venduti = ["smartphone", "tablet", "laptop", 
 #   "smartphone", "tablet", "smartwatch", "smartphone"]
 #Scrivi un programma in Python per determinare quante volte ciascun tipo di prodotto è stato venduto.
 #  Il programma deve stampare il numero di unità vendute per ciascun prodotto presente nella lista.

prodotti_venduti = ["smartphone", "tablet", "laptop","smartphone", "tablet", "smartwatch", "smartphone"]

def numero_unita(prodotti):
    prod = {}
    for prodotto in prodotti:
        if prodotto not in prod:
            prod[prodotto] = 1
        else:
            prod[prodotto] += 1
    print(prod)

numero_unita(prodotti_venduti)


# Lista dei prodotti venduti
prodotti_venduti = [
    "smartphone",
    "tablet",
    "laptop",
    "smartphone",
    "tablet",
    "smartwatch",
    "smartphone",
]

# Creazione di un set per trovare
# prodotti unici
prodotti_unici = set(prodotti_venduti)
prod = set(prodotti_venduti)

# Conteggio delle vendite per ciascun
# prodotto
for prodotto in prodotti_unici:
    conteggio = prodotti_venduti.count(prodotto)
    print(
        f"{prodotto}: {conteggio} unità vendute"
    )
    print("   ")
count = 0
for prodotto in prod:
    count += 1 
    print(f"{prodotto}: {count} unità vendute"
    )