class  LIBRO:
    def __init__(self,titolo,autore,prezzo):
        self.titolo = titolo
        self.autore = autore
        self.prezzo = prezzo
    
class LIBRERIA:
    def __init__(self):
        self.inventario = []
    #ADD BOOK
    def aggiungi_libro(self,book):
        self.inventario.append(book)
    #WATCH LIBRARY
    def mostra_libreria(self):
        print("Libreria:")
        for book in self.inventario:
            print(f"{book.titolo},{book.autore},{book.prezzo}€")
    #CALCULATE TOTAL EVERY BOOK IN INVENTORY
    def totale(self):
        somma = 0
        for book in self.inventario:
            somma += book.prezzo
        return f"Il totale è {somma}€"
    #FIND THE BOOK
    def find(self,parola:str):
        for book in self.inventario:
            if book.titolo.lower() ==  parola.lower():
                return f"Il titolo {book.titolo} è presente nel catalogo"
                break
            else:
                return f"Titolo non presente"
                break

######################################################
#MAIN
#####################################################
io = LIBRO("IO","Marracash",20)
tu = LIBRO("TU","Gue",100)
roccia_music = LIBRERIA()
roccia_music.aggiungi_libro(io)
roccia_music.mostra_libreria()
roccia_music.aggiungi_libro(tu)
roccia_music.mostra_libreria()
print(roccia_music.totale())
print(roccia_music.find("io"))
print(roccia_music.find("ioo"))