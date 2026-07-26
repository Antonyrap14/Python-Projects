# Immagina di lavorare come sviluppatore per una libreria.
#  Devi creare un programma che permetta agli utenti di cercare un libro all’interno del tuo database.
#  Il tuo database è una semplice lista di stringhe in Python,
#  dove ogni stringa è il titolo di un libro. Il tuo compito è scrivere una funzione,
#  chiamata ricerca_libro, che prenda in input la lista dei libri e una stringa chiave.
#  La funzione dovrebbe restituire una nuova lista contenente tutti i libri il cui titolo contiene
#  la parola chiave.
#  Ad esempio, dato:
#  libri = [
# ’Il Signore degli Anelli’,
#  ’Harry Potter e la Pietra Filosofale’,
#  ’Il gioco del trono’,
#  ’La ragione della vita’]

#  e la parola chiave ’la’,
#la funzione dovrebbe restituire 
# [’Il Signore degli Anelli’, ’Harry Potter e la Pietra Filosofale’, ’La ragione della vita’].


libri = [
    "Il Signore degli Anelli",
    'Harry Potter e la Pietra Filosofale',
    'Il gioco del trono',
    'La ragione della vita' 
    ]

def ricerca_libro(lista,parola):
    ricercati = []

    for stringa in lista:
        if parola in stringa:
            ricercati.append(stringa)

    if len(ricercati) == 0:
        print("Non sono stati trovati libri associati!")
    else:
        print(f"Libri trovati:\n {ricercati}")

while(True):
    scelta = input("vuoi cercare nel db il libro tramite una parola? s/n ")
    if scelta == "s":
        parola = input("inserisci una parola:")
        ricerca_libro(libri,parola)
    else:
        print("Va bene grazie!")
        break


