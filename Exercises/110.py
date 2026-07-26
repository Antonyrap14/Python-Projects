def spedizioni(prezzo):
    if prezzo >= 50:
        return f"La spedizione è gratuita, il costo è solo {prezzo}"
    else:
        costo = prezzo + 5
        return f"La spedizione costa 5 euro, il totale è {costo}"

prezzo = int(input("scrivi il prezzo:"))
print(spedizioni(prezzo))