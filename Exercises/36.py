studenti = {}
#aggiunta studente
def aggiungi(studenti):
    nome = input("Inserisci il nome:")
    if nome not in studenti:
        votazione = int(input("inserisci il voto:"))
        studenti[nome] = votazione
        print(f"Aggiunto il voto {votazione} per lo studente {nome}")
    else:
        print("Utente già presente!")
#aggiornare voto
def nuovoVoto(studenti):
    nome = input("inserisci il nome dello studente che vuoi aggiornare:")
    if nome not in studenti:
        print("studente non presente..")
    else:
        voto = int(input("inserisci un voto:"))
        studenti[nome] = voto
        print(f"Aggiunto il voto {voto} per lo studente {nome}")
#calcolare media dei voti
def media(studenti):
    somma = 0
    for nome,voto in studenti.items():
        somma += voto
    media = somma / len(studenti)
    return media
#menu
def menu():
    while(True):
        scegli = int(input("inserisci 1 per aggiungere studente, 2 per aggiornare il voto, 3 per calcolare la media"))
        if scegli == 1:
            aggiungi(studenti)
        elif scegli == 2:
            nuovoVoto(studenti)
        elif scegli == 3:
            print(media(studenti))
        else:
            print("programma finito...")
            break

menu()

