# Ti trovi a lavorare per un negozio di libri e ti è stato chiesto di creare un programma in Python
#  per tenere traccia dei titoli dei libri venduti giorno per giorno. Ogni giorno,
#  ti viene data una lista di tutti i titoli dei libri venduti. Il tuo compito è contare quanti volte
#  ogni titolo è stato venduto. Crea una funzione che accetta una lista di titoli di libri come argomento
#  e restituisce un dizionario che conta il numero di volte che ogni libro è stato venduto.

libri = ["harry","potter","potter","potter","cucina","era","are"]

def conta_libri(libri):
    dizionario = {}
    for elemento in libri:
        if elemento not in dizionario:
            dizionario[elemento] = 1
        else:
            dizionario[elemento] += 1
    return dizionario


print(conta_libri(libri))
    
            

    
