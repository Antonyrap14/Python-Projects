# Immagina di essere un bibliotecario e di avere una lista dei libri che ritornano in biblioteca.
#  Ogni libro è rappresentato dal suo titolo. Alcuni titoli possono essere ripetuti,
#  dato che ci sono molte copie dello stesso libro.
#  Il tuo compito è quello di contare il numero di copie di ogni libro nella lista.
#  Supporre che la lista dei libri sia data come segue:

#  libri = ["Il Piccolo Principe", "1984", 
#"Il Piccolo Principe", "Il Signore degli Anelli", 
#"Moby Dick", "1984", 
# "1984", "La Divina Commedia", 
# "Il Piccolo Principe"]

# Sviluppa una funzione in Python chiamata conteggiolibri che conta il
#  numero di ogni libro nella lista e restituisce un dizionario.
#  La chiave del dizionario dovrebbe essere il titolo del libro e
#  il valore dovrebbe essere il conteggio per quel titolo specifico.

libri = ["Il Piccolo Principe", "1984", "Il Piccolo Principe", "Il Signore degli Anelli", "Moby Dick", "1984","1984", "La Divina Commedia", "Il Piccolo Principe"]

def conta_libro(libri):
    dizionario = {}
    for elemento in libri:
        if elemento not in dizionario:
           dizionario[elemento] = 1
        else:
            dizionario[elemento] += 1
    return dizionario

print(conta_libro(libri)) 

