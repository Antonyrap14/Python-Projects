#Sei lo sviluppatore di un sistema di prenotazione di un cinema multisala. 
# Durante ogni iterazione del tuo software, ottieni una lista di film in programmazione
#  per il giorno successivo. Purtroppo, uno dei proiettori è guasto e non sarà possibile
#  mostrare il film in programmazione per la sala 3. Usando Python, come rimuoveresti il
#  film associato alla sala guasta dalla lista, dato che sappiamo che la sala 3 corrisponde all’indice 2
#  della lista?

film = ["era glaciale2", "pinocchio","harry potter 3","san valentino di sangue","amore a prima vista"]

def prenotazione(film):
    nome = input("Inserisci il tuo nome:")
    scegli = int(input("scegli il film"))
    if scegli == 2:
        print(f"mi spiace non puoi prenotare il film {film[2]}")
        film.pop(2)
    else:
        print(f"il film che hai scelto è: {film[scegli]}\nha prenotato {nome}")
        del film[2]
    print(film)

prenotazione(film)
