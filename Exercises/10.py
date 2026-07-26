#Supponiamo di avere un elenco di studenti che partecipano a un corso di linguaggio Python.
#  L’elenco è presente in una lista in cui ogni elemento rappresenta lo studente in ordine di registrazione.
#  Per esempio, students = [’Mario’, ’Giovanni’, ’Luca’, ’Marco’, ’Francesco’].
#  Il direttore del corso ha deciso di cancellare le registrazioni degli studenti in posizione di indice pari,
#  a partire dall’indice 0.
#  Scrivere una funzione in Python chiamata delete_students()
#  che prenda in input la lista degli studenti e rimuova gli studenti nelle posizioni di indice pari.
#  La funzione deve restituire la lista aggiornata.
def delete_students(students):
    del students[::2]
    return students

students = [
    "Mario",
    "Giovanni",
    "Luca",
    "Marco",
    "Francesco",
]
print(delete_students(students))

