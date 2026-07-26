class Libro:
    def __init__(self, titolo, autore, anno_pubblicazione):
        self.titolo = titolo
        self.autore = autore
        self.anno_pubblicazione = anno_pubblicazione
        

    def __str__(self):
        return f"{self.titolo} di {self.autore} ({self.anno_pubblicazione})"

class Membro:
    def __init__(self, nome):
        self.nome = nome
        self.libri_prestito = []

    def aggiungi_libro(self, libro):
        self.libri_prestito.append(libro)

    def restituisci_libro(self, libro):
        self.libri_prestito.remove(libro)

    @property
    def num_libri_prestito(self):
        return len(self.libri_prestito)

    def __str__(self):
        return self.nome

class Biblioteca:
    def __init__(self):
        self.catalogo = []

    def aggiungi_libro(self, libro):
        self.catalogo.append(libro)

    def rimuovi_libro(self, libro):
        self.catalogo.remove(libro)

    def mostra_catalogo(self):
        print("Catalogo della Biblioteca:")
        for libro in self.catalogo:
            print(libro)

# Funzione principale per testare la soluzione
def main():
    # Creazione libri
    libro1 = Libro("1984", "George Orwell", 1949)
    libro2 = Libro("To Kill a Mockingbird",
        "Harper Lee",1960)
    libro3 = Libro("Il Signore degli Anelli",
        "J.R.R. Tolkien",1954)

    # Creazione biblioteca e aggiunta libri
    biblioteca = Biblioteca()
    biblioteca.aggiungi_libro(libro1)
    biblioteca.aggiungi_libro(libro2)
    biblioteca.aggiungi_libro(libro3)

    # Creazione membri
    membro1 = Membro("Alice")
    membro2 = Membro("Bob")

    # Mostra catalogo
    biblioteca.mostra_catalogo()

    # Prestito di libri
    membro1.aggiungi_libro(libro1)
    biblioteca.rimuovi_libro(libro1)
    print(
        f"\n{membro1.nome} ha preso: {libro1}"
    )
    biblioteca.mostra_catalogo()

    # Restituzione di libri
    membro1.restituisci_libro(libro1)
    biblioteca.aggiungi_libro(libro1)
    print(
        f"\n{membro1.nome} ha restituito: {libro1}"
    )
    biblioteca.mostra_catalogo()

main()




