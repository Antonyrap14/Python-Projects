nuova_prenotazione = True
prenotazioni = []

while(nuova_prenotazione):
    choose = input("vuoi inserire un nome? ")
    if choose.lower() == "si":
        nome = input("inserisci il nome:")
        prenotazioni.append(nome)
    else:
        print("Va bene ciaoooo")
        nuova_prenotazione = False

print("I nomi delle persone che hanno prenotato:")

for elemento in prenotazioni:
    print(elemento)


