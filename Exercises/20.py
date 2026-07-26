# L’Università ha un sistema per gestire gli studenti iscritti.
#  Ogni studente è rappresentato da un dizionario contenente il nome,
#  cognome e l’annodiiscrizione. Tutti gli studenti sono salvati in una lista chiamata studentiuniversità.
#  Hai il compito di scrivere una funzione, cercastudente, che prenda come input una listadistudenti e un
#  nomestudente e che restituisce una lista con tutti gli studenti che hanno quel nome.



studente = {
    "nome":"Riccardo",
    "cognome":"Paolo",
    "anno":"2020"
}
studente0 = {
    "nome":"Pino",
    "cognome":"Pini",
    "anno":"2022"
}

studente1 = {
    "nome":"Pino",
    "cognome":"Pluto",
    "anno":"2021"
}

studentiuniversità = [studente,studente0,studente1]

def cerca_studenti (studenti,nome):
    lista = []
    for studente in studenti:
        if nome == studente["nome"]:
            lista.append(studente)
    for n in lista:
        print(n)
cerca_studenti(studentiuniversità,"Pino")

