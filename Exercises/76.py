temperature = [
    ("Firenze", 20),
    ("Roma", 25),
    ("Milano", 18),
    ("Napoli", 22)
]
print(temperature)

for citta,gradi in temperature:
        print(f"citta:{citta}")
        print(f"temperatura:{gradi}")

def genera_riepilogo(temperature):
    # Lista per memorizzare le parti della stringa
    riepilogo_parti = ["Oggi le temperature sono:"]

    # Ciclo attraverso ogni coppia (città,
    # temperatura) nella lista di tuple
    for citta, temp in temperature:
        # Aggiungi la stringa formattata per ogni
        # città e temperatura
        riepilogo_parti.append(f"{citta} {temp} gradi")

    # Unisci tutte le parti in una singola stringa
    # separata da virgole
    riepilogo = ", ".join(riepilogo_parti[1:])

    return riepilogo_parti[0] + " " + riepilogo

# Esempio d’uso della funzione
temperature = [
    ("Firenze", 20),
    ("Roma", 25),
    ("Milano", 18),
    ("Napoli", 22),
]
print(genera_riepilogo(temperature))


