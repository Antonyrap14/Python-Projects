def prodotti(prodotti_magazzino):
    prodotti = len(prodotti_magazzino)
    if prodotti < 10:
        return "Necessita di prodotti poichè ce ne sono meno di 10"
    elif prodotti >= 10 and prodotti < 20:
        return "Abbiamo abbastanza prodotti"
    elif prodotti > 20:
        return "Magazzino quasi pieno"
lista = ["pane","qui","acqua","p","a","b","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a","a"]
print(prodotti(lista))