def prezzo_totale(prezzo_base,quantita,sconto=0):
    totale = 0
    quantita_da_togliere = prezzo_base * quantita * (sconto/100)
    prezzo_finale = prezzo_base -quantita_da_togliere

    if sconto > 50:
        return "Sconto troppo alto"
    else:
        return f"Prezzo iniziale {prezzo_base}, di cui togliere {quantita_da_togliere}\n---------------------------------------------\nPrezzo finale {prezzo_finale}"
print(prezzo_totale(20,3,55))
print(prezzo_totale(20,3))
print(prezzo_totale(20,3,23))

