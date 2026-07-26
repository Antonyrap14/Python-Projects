dizionario = {
    "A1":2,
    "A2":3,
    "A3":1
}

def add(dizionario):
    while(True):
        aggiungi = input("vuoi aggiungere un prodotto??")
        if aggiungi == "si":
            elemento = input("inserisci elemento:")
            quantita = int(input("inserisci quantita:"))
            dizionario[elemento] = quantita
        else:
            print(f"Il dizionario è:{dizionario}")
            break

add(dizionario)