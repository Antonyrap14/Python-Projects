# Stai lavorando su un sistema di gestione di una biblioteca virtuale.
#  Ogni libro è rappresentato come un dizionario con chiavi ’titolo’, ’autore’ e ’anno di pubblicazione’.
#  Tutti i libri sono memorizzati in una lista. Tuttavia, alcuni libri sono duplicati e si desidera eliminare
#  i duplicati. Scrivi una funzione denominata rimuovi_duplicati che prende la lista dei libri come input e
#  rimuove i libri duplicati basandosi sul titolo.
#  La funzione deve restituire la lista dei libri dopo la rimozione dei duplicati.

libro = {
    "titolo":"harry",
    "autore":"potter",
    "anno": 2010
}
libro1 = {
    "titolo":"era",
    "autore":"probi",
    "anno": 2009
}
libro2 = {
    "titolo":"piccoli",
    "autore":"brividi",
    "anno": 1990
}
libro3 = {
    "titolo":"era",
    "autore":"glaciale",
    "anno": 2003
}
libro4 = {
    "titolo":"harry",
    "autore":"potter",
    "anno": 2010
}

lista = [libro,libro2,libro1,libro3,libro4]
nuova_lista = []

def elimina_duplicati(lista):
    for libro in lista:
        if libro not in  nuova_lista:
            nuova_lista.append(libro)
            print(f"libro:{libro} aggiunto alla lista")
        else:
            continue
    
    for e in nuova_lista:
        print(e['titolo'])

    #for elemento in nuova_lista:
        #print(f"libro {elemento["titolo"]}\n")

elimina_duplicati(lista)
    
