codici = {"c1","c2","c3"}
lista = ["a1","a2","a3"]

def aggiungi_codice(set,lista):
    for valore in lista:
        set.add(valore)
    return set

print(aggiungi_codice(codici,lista))