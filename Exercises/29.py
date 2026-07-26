# Immagina di lavorare per un’organizzazione sportiva e di avere una lista dei tempi dei corridori in una gara.
#  Hai bisogno di ordinare tali tempi in ordine crescente per determinare la classifica del podio.
#  La lista si presenta così:
# L’obiettivo dell’esercizio è scrivere una funzione in Python che possa ordinare questa lista in ordine crescente.
#  Per semplificare, si può assumere che i tempi siano sempre espressi nel formato HH:MM:SS.

def ordina_tempi(tempi):
    # Converti la lista dei tempi in una lista di tuple, 
    # dove ogni tupla è formata dal tempo come stringa 
    # e come intero in secondi
    tempi = [(t,
            sum(int(x) * 60**i
                for i, x in enumerate(
                    reversed(t.split(":"))
                )
)
        ) for t in tempi
    ]

    # Ordina la lista di tuple in base al secondo 
    # elemento di ogni tupla (il tempo in secondi)
    tempi.sort(key=lambda x: x[1])

    # Restituisci una lista ordinata dei soli tempi 
    return [t[0] for t in tempi]

tempi_corridori = [
    "1:34:02","1:42:09","1:33:56",
    "1:28:33","1:45:45","1:37:27",
]
tempi_corridori_ordinati = ordina_tempi(
    tempi_corridori
)

print(tempi_corridori_ordinati)

 
