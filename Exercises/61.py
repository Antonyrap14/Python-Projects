libri = {"harry potter","Era glaciale","Stranger Things","Hermione","Ron"}
lista = ["Era glaciale","Ron"]

def rimuovi(libri,lista):
    for elemento in lista:
        libri.discard(elemento)
    return libri

print(rimuovi(libri,lista))