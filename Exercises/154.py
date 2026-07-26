def prezzo_finale(prezzo, tassa=22, sconto=0):
    prezzo_scontato = prezzo - (prezzo * sconto / 100)
    prezzo_tassato = prezzo_scontato + (prezzo_scontato * tassa / 100)
    return prezzo_tassato

# MAIN
prezzo = int(input("Inserisci prezzo: "))

tassa_input = input("Inserisci tassa (Invio per 22%): ")
sconto_input = input("Inserisci sconto (Invio per 0%): ")

tassa = int(tassa_input) if tassa_input else 22
sconto = int(sconto_input) if sconto_input else 0

print(prezzo_finale(prezzo, tassa, sconto))

print(prezzo_finale(100))