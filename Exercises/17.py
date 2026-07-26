# Sei un responsabile del reparto di Risorse Umane di una grande azienda.
#  Hai una lista con i nomi dei dipendenti.
#  Devi scrivere una funzione in Python che prende come input il nome di un dipendente e ti dice se quel dipendente
#  è o non è nella lista.
#  È importante che la funzione sia di facile utilizzo e reperisca l’informazione richiesta 
#  nel minor tempo possibile.

dipendenti = ["massimo","mario","biagio","antonio","chiara","genoveffa","giorgia"]

def cerca(dipendenti,nome):
    if nome in dipendenti:
        return True
    else:
        return False

if cerca(dipendenti,"antonio") == True:
    print(f"trovato dipendente")
else:
    print("mi spiace")
        