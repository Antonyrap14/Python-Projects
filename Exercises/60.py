inventario = {"pallone","racchette","palline"}
lista = ["palla","rete","palla","palo"]

def aggiungi(lista):
    for elemento in lista:
        inventario.add(elemento)
    print(inventario)

aggiungi(lista)