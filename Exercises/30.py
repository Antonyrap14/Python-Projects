# Supponiamo di essere un bibliotecario,
#  e abbiamo un elenco di libri rappresentato tramite una lista di stringhe in Python.
#  Ogni libro è rappresentato dal suo titolo.
#  Ovviamente, per facilitare il lavoro e la ricerca nella biblioteca,
#  ci piacerebbe ordinare la lista dei libri in ordine alfabetico.
#  Il tuo compito è scrivere un programma Python che prenda in ingresso una lista non ordinata di titoli di libri
#  e restituisca la stessa lista, ma con i titoli ordinati in ordine alfabetico.

libri = ["harry","potter","era","are","la grande P"]

def ordina(libri):
    print(sorted(libri))

ordina(libri)