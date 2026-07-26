clienti = {
    "marco":{
        "pizza":20.5,
        "acqua":1.5,
        "dolce":6
    },
    "pio":{
        "pizza":21,
        "acqua":1.5,
        "amaro":4
    },
    "federico":{
        "pasta":8,
        "acqua":1.5,
        "cocacola":3.5,
        "dolce":6
    }
}

def nuovo_ordine(dizionario,ordine,cliente):
    for client,dettagli in dizionario.items():
        if client == cliente:
            prezzo = int(input("inserisci prezzo:"))
            dettagli[ordine] = prezzo
            break
    print(dizionario)

nuovo_ordine(clienti,"sushi","marco")                   

def somma(dizionario,nome):
    somma = 0
    for elemento,dettagli in dizionario.items():
        for cibo,prezzo in dettagli.items():
            if elemento == nome:
                somma += prezzo
    print(f"Il cliente{nome} ha speso:{somma}")

somma(clienti,"marco")

