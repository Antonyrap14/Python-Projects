def spesa():
    lista = []
    while(True):
        quantita = input("inserisci quantita:")
        prezzo = input("inserisci prezzo:")

        if quantita != "" or prezzo != "":
            prezzo = int(prezzo)
            quantita = int(quantita)
            tupla = (prezzo,quantita)
            lista.append(tupla)
        else:
            break
    return(lista)

def totale(quantita,prezzo):
    totale = quantita * prezzo
    return totale

def new_list(lista):
    new = [
        f"Il totale per la spesa di {elemento[0]} e {elemento[1]} e di: {totale(elemento[0],elemento[1])}" for elemento in lista
    ]
    print(new)


new_list(spesa())


def calculatetotalspent(transactions):
    messages = []
    
    for i, transaction in enumerate(transactions, start=1):
        total = 0
        for quantity, unit_price in transaction:
            total += quantity * unit_price
        
        # Arrotondamento a due decimali
        total = round(total, 2)
        
        message = f"Totale spesa per la transazione {i}: {total}€."
        messages.append(message)
    
    return messages

        