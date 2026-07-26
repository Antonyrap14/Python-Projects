def prezzoFinale(prezzo,sconto=10,iva=22):
    totale = ((prezzo - (prezzo * sconto/100))*iva/100) + prezzo
    return totale

lista = [22,345,200,100,50]


new_lista = [
   prezzoFinale(elemento) for elemento in lista
]
print(new_lista)