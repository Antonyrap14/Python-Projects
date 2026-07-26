class Book:
    def __init__(self, titolo, autore, anno, disponibile=True):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.disponibile = disponibile
    
    def borrow(self):
        if self.disponibile:
            self.disponibile = False
            print("Libro preso in prestito")
        else:
            print("Libro non disponibile")

    def return_book(self):
        if not self.disponibile:
            self.disponibile = True
            print("Libro restituito, ora disponibile")
        else:
            print("Il libro era già disponibile")

    @property
    def info(self):
        availability = (
            "disponibile"
            if self.disponibile
            else "non disponibile"
        )
        return f"Titolo: {self.titolo}, Autore: {self.autore}, Anno: {self.anno}, Disponibilità: {availability}"


libro = Book("Ora che non ho", "Io", 1999)
libro.borrow()
print(libro.info)