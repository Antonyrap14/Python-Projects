# I dati riguardanti il punteggio dei partecipanti ad un gioco sono salvati in una lista non ordinata
# chiamata scores.
#  Per varie necessità, è necessario ordinare la lista sia in ordine ascendente che discendente.
#  Il tuo compito è scrivere un codice Python che ordeni la lista scores nell’ordine:
#  ascendente ed in seguito discendente.

scores = [22,23,4,25,44,91,23,33,12,20]

def riordina(lista):
    scores.sort(
    lambda x:x, reverse= True
    )

riordina(scores)