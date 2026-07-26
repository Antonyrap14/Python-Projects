#Siete stati assunti come sviluppatori di software per una piccola impresa.
#  I vostri colleghi vi consegnano una lista di prodotti immagazzinati in un magazzino sottodimensionato
#  ed è vostro compito consolidare l’inventario eliminando i duplicati.
#  La lista di prodotti è contenuta in un file di testo in cui ogni riga è un prodotto e può avere duplicati.

prodotti = ["mela","pera","banana","mela","arancia","pesca","banana"]

def elimina_duplcati(prodotti):
    lista = []
    for prodotto in prodotti:
        if prodotto in lista:
            continue
        else:
            lista.append(prodotto)
    return lista        

print(elimina_duplcati(prodotti))
    
# Il vostro compito è scrivere un programma in Python che legge il file di testo
#  contenente l’elenco dei prodotti, rimuove i duplicati dalla lista e scrive il risultato in un nuovo
#  file di testo.

def remove_duplicates():
    # Apriamo il file "prodotti.txt" in
    # modalità lettura
    with open("prodotti.txt", "r") as file:
        products = file.readlines()

    # Rimuoviamo gli spazi bianchi da
    # ogni riga
    products = [
        product.strip() for product in products
    ]

    # Creiamo una lista di prodotti
    # unici usando un set
    unique_products = list(set(products))

    # Scriviamo i prodotti unici nel
    # file "prodotti_unici.txt"
    with open("prodotti_unici.txt", "w") as file:
        for product in unique_products:
            file.write(product + "\n")

# Chiamiamo la funzione per rimuovere i
# duplicati
remove_duplicates()

