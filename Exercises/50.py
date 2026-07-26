clienti = {
    "001": {"nome": "Mario Rossi", 
            "età": 34, "indirizzo": "Via Roma 1"},
    "002": {"nome": "Laura Bianchi", 
            "età": 29, "indirizzo": "Via Milano 45"},
    "003": {"nome": "Giuseppe Verdi", 
            "età": 40, "indirizzo": "Via Napoli 12"}
}

def elimina(dizionario,prodotto):
    if prodotto in dizionario:
        del dizionario[prodotto]
        print(clienti)
    else:
        print("Non puoi a Cops")

elimina(clienti,"002")