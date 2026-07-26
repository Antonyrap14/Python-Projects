testo = """La programmazione con Python è interessante.

Gli sviluppatori Python possono fare molte cose.

È importante conoscere bene Python per essere produttivi."""
parola_chiave = "Python"

def cerca(testo,paola_chiave):
    lista = []
    text = testo.split("\n")
    parola_chiave_lower = parola_chiave.lower()

    for indice,linea in enumerate(text):
        if parola_chiave_lower in linea.lower():
           lista.append((indice + 1, linea))
    return(lista)

print(cerca(testo,parola_chiave))

#########################################################
def ricerca_parola_chiave(testo, parola_chiave):
    risultato = []
    linee = testo.split("\n")
    parola_chiave_lower = parola_chiave.lower()

    for indice, linea in enumerate(linee):
        if parola_chiave_lower in linea.lower():
            risultato.append((indice + 1, linea))

    return risultato

# Esempio di utilizzo

testo = """La programmazione con Python è interessante.
Gli sviluppatori Python possono fare molte cose.
È importante conoscere bene Python per essere produttivi."""
parola_chiave = "python"

print(ricerca_parola_chiave(testo, parola_chiave))

