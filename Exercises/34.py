# Supponiamo di gestire una scuola e di mantenere una lista degli studenti.
#  Durante la semestrale registrazione di nuovi studenti, dobbiamo inserire i nuovi studenti nella lista esistente 
# senza perdere l’ordine alfabetico. Considerando una lista di studenti già in ordine alfabetico come 
# studenti = [’Alice’, ’Bob’, ’Charlie’, ’Dave’],
#  scrivete un programma che chieda all’utente un nuovo nome studente e lo inserisca al posto giusto nella lista.
studenti = ["Alice","Bob","Charlie","Dave"]

def inserisci(studenti):
    nome = input("inserisci il nome dello studente:")
    studenti.insert(1,nome)
    sorted(studenti)
    print(studenti)

inserisci(studenti)

#############################################################
studenti = ["Alice", "Bob", "Charlie", "Dave"]

# L’utente inserisce il nome del nuovo
# studente
nuovo_studente = input(
    "Inserisci il nome del nuovo studente: "
)

# Trova l’indice in cui inserire il
# nuovo studente per mantenere l’ordine
# alfabetico
indice = 0
while (
    indice < len(studenti)
    and nuovo_studente > studenti[indice]
):
    indice += 1

# Inserisci il nuovo studente nella
# posizione corretta
studenti.insert(indice, nuovo_studente)

print(studenti)

