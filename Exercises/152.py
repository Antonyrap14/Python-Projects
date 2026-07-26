def prenotazione(attivita,durata=None):
    if attivita == "yoga":
        durata = 45 if durata is None else durata
    elif attivita == "spinning":
        durata = 30 if durata is None else durata
    else:
        durata = 30 if durata is None else durata
    print(f"{attivita}:{durata}")

attivita = input("inserisci attivita:")
durata = (input("inserisci durata:"))

if durata:
    durata = int(durata)
else:
    durata = None

prenotazione(attivita,durata)
