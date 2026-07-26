# Supponiamo di avere una lista di studenti iscritti a un corso universitario.
#  Ogni studente è rappresentato da una stringa che contiene il suo cognome.
#  La lista è organizzata in modo tale che l’indice di ciascun elemento corrisponde al numero di 
# registrazione dello studente. Ad esempio, l’indice 0 corrisponde al primo studente iscritto,
#  l’indice 1 al secondo studente e così via. Supponiamo che alcuni studenti abbiano deciso di abbandonare
#  il corso e di conseguenza, bisogna rimuoverli dalla lista. Il tuo compito è di scrivere una funzione Python
#  che prenda due argomenti: la lista degli studenti e una lista di indici.
#  La funzione dovrebbe rimuovere gli studenti corrispondenti a questi indici dalla lista
#  e restituire la lista aggiornata.

indici = [1,2,3,4]
studenti = ["a","b","c","d"]

def elimina(lista,lista1):
    while(True):
        s = input("Vuoi eliminare qualcuno? s/n ")
        if s == "s":
          scegli = int(input("elimina studente dall'indice: "))
          del lista1[scegli]
        else:
           print(studenti)
           break
   

elimina(indici,studenti)
