# Hai una lista, fruits, con vari frutti disponibili nel tuo supermercato preferito.
#  Durante una chiamata, il tuo fornitore ti informa che alcune tipologie di frutta non sono più disponibili.
#  Così, è necessario rimuoverle dalla lista.
#  La tua lista iniziale di frutta è: [’apple’, ’banana’, ’mango’, ’grape’, ’orange’, ’watermelon’, ’peach’].
#  I frutti indicati dal fornitore per le quali non c’è disponibilità sono:
#  unavailablefruits = [’mango’, ’peach’, ’watermelon’].
#  Il tuo compito è quello di scrivere un programma Python per rimuovere i frutti
#  non disponibili dalla lista fruits.
#  Nota che i frutti non disponibili possono cambiare,
#  quindi il tuo codice deve essere flessibile per consentire l’aggiunta o la rimozione dei frutti
# nella lista unavailablefruits.

supermercato = ["mela","banana","mango","arancia","melone","pesca"]
non_disponibili = ["mango","pesca","melone"]

def rimuovi_frutti(supermercato):
    nuovosupe = []
    while(True):
        scegli = input("vuoi verificare quale frutta  è disponibile? s/n ")
        if scegli == "s":
            for elemento in supermercato:
                if elemento not in non_disponibili:
                    nuovosupe.append(elemento)
            print(nuovosupe)
            break
        else:
            print("Va bene non c'è nessun problema")
            break
    

def aggiorna(lista):
    while (True):
        scegli = input("Scegli se vuoi aggiungere o rimuovere elementi a/r ")

        if scegli == "a":
            elemento = input("scrivi l'elemento che vuoi aggiungere: ")
            lista.append(elemento)

        elif scegli == "r":
            elemento = input("scrivi l'elemento che vuoi rimuovere: ")
            lista.remove(elemento)    
        
        else:
            rimuovi_frutti(supermercato)
            break
        
      
# MAIN
scegli = input("Vuoi rimuovere gli elementi della lista o aggiornare la lista? r/a ")

if scegli == "r":
    rimuovi_frutti(supermercato)

elif scegli == "a":
    aggiorna(non_disponibili)

else:
    print("Ciaooo")

            


