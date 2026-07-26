#Per i clienti di età inferiore ai 18 anni, il conto è gratuito.
#   Per i clienti di età compresa tra 18 e 25 anni, il costo è di 3 Euro al mese.
#   Per i clienti di età compresa tra 26 e 65 anni, il costo è di 10 Euro al mese.
#   Per i clienti con più di 65 anni, il costo è di 5 Euro al mese.

def prezzi(eta):
    tariffa = 0

    if eta < 18:
        tariffa = 0
    elif 18 <= eta <= 25:
        tariffa = 3
    elif 26 <= eta < 65:
        tariffa = 10
    else:
        tariffa = 5
    
    if tariffa == 0:
        return "Il conto non ha costi mensili"
    else:
        return f"Il prezzo è di {tariffa} al mese"
    
eta = int(input("Inserisci eta:"))
print(prezzi(eta))
    
    
