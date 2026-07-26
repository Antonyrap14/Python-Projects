# Supponiamo di avere una lista di nomi di studenti di una classe.
#  Ogni studente può essere presente più volte, in quanto rappresenta la quantità di volte che lo studente
#  ha seguito la lezione. Il tuo compito è scrivere un programma Python che conteggi il
#numero di volte che ogni studente è presente nella lista e restituisca il risultato in un dizionario,
#  dove la chiave è il nome dello studente e il valore è il conteggio.
#  Ad esempio, data la lista: ["Anna", "Marco", "Anna",
#  "Marco", "Marco", "Giulia",
#  "Giulia", "Giulia", "Luca"]
# Il tuo programma dovrebbe produrre il seguente output: {"Anna": 2, "Marco": 3, "Giulia": 3, "Luca": 1}

studenti = ["Anna", "Marco", "Anna","Marco", "Marco", "Giulia","Giulia", "Giulia", "Luca"]

def conteggi(lista):
    dizionario = {}

    for elemento in lista:
        count = 0
        if elemento not in dizionario:
            count = 1
            dizionario[elemento] = count
        else:
            dizionario[elemento] += count + 1
    
    return dizionario

print(conteggi(studenti))
        
        
        

