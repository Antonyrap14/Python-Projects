partecipanti = {'Alice', 'Bob', 'Charlie', 'Diana'}
darimuovere = ['Bob', 'Diana']

def rimuovi(seet,lista):
    for nome in lista:
        seet.discard(nome)
    print(seet)
    
rimuovi(partecipanti,darimuovere)