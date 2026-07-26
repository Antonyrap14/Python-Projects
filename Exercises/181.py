prezzi_netto = [100, 250, 50, 75, 125]

def calcola_iva(prezzi):
    prezzo_lordo = [
        round((prezzo * 0.22 + prezzo),2) for prezzo in prezzi 
    ]
    return f"Prezzi lordi:\n{prezzo_lordo}"

print(calcola_iva(prezzi_netto))