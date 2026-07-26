def sconto(totale):
    if totale > 20:
        sconto = totale * 0.1
        new_totale = totale - sconto
        return f"Dato che il conto è di {totale} e supera i 20 euro abbiamo applicato lo sconto del 10%.\nIl nuovo totale è {new_totale}"
    else:
        return f"Il conto da pagare è di {totale}"

totale = float(input("inserisci totale:"))
print(sconto(totale))