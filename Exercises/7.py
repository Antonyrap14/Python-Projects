#Supponi di gestire una biblioteca e di avere una lista di libri disponibili.
#  Tuttavia, alcuni libri sono stati restituiti danneggiati e non possono più essere prestati,
#  quindi devono essere rimossi dalla tua lista. Hai l’elenco degli indici dei libri da rimuovere nella tua lista.
#  La tua lista di libri è la seguente: libri = [’Il nome della rosa’,
#  ’Il vecchio e il mare’, ’Il codice Da Vinci’, ’Il grande Gatsby’, ’Il signore degli anelli’]
#  E gli indici da rimuovere sono: indici = [1,3] Come faresti per rimuovere questi libri dalla lista?

libri = [
    "Il nome della rosa",
    "Il vecchio e il mare", 
    "Il codice Da Vinci",
    "Il grande Gatsby",
    "Il signore degli anelli"
    ]

dimensione = len(libri)

for i in range(dimensione):
    if i == 2:
        del libri[2]
for i in range(dimensione):
    if i == 0:
        del libri[i]
print(libri)