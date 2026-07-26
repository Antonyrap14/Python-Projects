#  Immagina di lavorare in una biblioteca e abbiamo un lungo elenco di libri.
#  Ogni libro è rappresentato come una stringa che include il titolo, l’autore e l’anno di pubblicazione,
#  ogni elemento separato da una virgola, per esempio, Lord of the Rings, J.R.R. Tolkien, 1954.
#  La lista dei libri può essere molto lunga (decine di migliaia di libri).
#  Scrivi un programma usando Python che permette a un utente di cercare un libro per titolo, l’autore o l’anno di
#  pubblicazione.

def find_book(book_list, search_term):
    # crea una lista vuota per i
    # risultati di ricerca
    search_results = []

    # scansiona ogni libro nella lista
    for book in book_list:
        # se il termine di ricerca è nel
        # libro, aggiungilo ai risultati
        # di ricerca
        if search_term in book:
            search_results.append(book)

    return search_results

# lista di libri
book_list = [
    "Lord of the Rings, J.R.R. Tolkien, 1954",
    "Harry Potter, J.K. Rowling, 1997",
    "Game of Thrones, George R. R. Martin, 1996",
]

# cerca i libri da J.R.R. Tolkien
print(find_book(book_list, "J.R.R. Tolkien"))

