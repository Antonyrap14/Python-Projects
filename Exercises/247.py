class libro:
    def __init__(self,titolo,autore,anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno

    @property
    def __str__(self):
        return f"Il libro {self.titolo}, di {self.autore} dell'anno {self.anno}"

class membro:
    def __init__(self,nome,lista_libri):
        self.nome = nome
        self.lista_libri = lista_libri

    def aggiungi_libr0(self,book):
        return self.lista_libri.append(book)

    def return_libro(self,book):
        return self.lista_libri.remove(book)
    @property
    def numero_libri(self):
        return len(self.lista_libri)

book = libro("Jack","io",1999)
print(book.__str__)
lista = []
m = membro("Jack",lista)
m.aggiungi_libr0("io")
m.aggiungi_libr0("tu")
print(m.numero_libri)
m.return_libro("io")
print(m.numero_libri)