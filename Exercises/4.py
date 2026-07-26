#Supponiamo di essere in una biblioteca dove hai due elenchi di libri. 
# Il primo elenco (elenco A) contiene i libri che la biblioteca possiede attualmente e 
# il secondo elenco (elenco B) contiene i nuovi libri che la biblioteca ha acquistato.
# Il tuo compito sarà scrivere un programma Python che estenda l’elenco A con i libri nell’elenco B.

a = ["pippo","topolino","pluto"]
b = ["nuovopippo","nuovotopolino","nuovopluto"]

a.extend(b)

print(a)