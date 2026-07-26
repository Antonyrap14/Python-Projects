# Siete i proprietari di un negozio di abbigliamento online e avete una lista con i nomi dei vostri prodotti.
#  Avete appena lanciato un nuovo prodotto Giacca in Jeans che deve essere posizionato al primo posto nel vostro
#  inventario online. Potete utilizzare il metodo insert() di Python per aggiungere Giacca in Jeans all’inizio
#  della lista.
# La missione è scrivere un codice Python per inserire Giacca
#  in Jeans nella posizione corretta all’interno della lista di prodotti esistente.

lista = ["maglia","pullover","pantaloni","tuta"]
elemento = "giacca in jeans"
posizione = lista.index("maglia")
lista.insert(posizione,elemento)
print(lista)


