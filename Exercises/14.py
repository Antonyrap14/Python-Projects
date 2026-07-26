# Immagina di avere un ristorante e di utilizzare Python per gestire l’inventario degli articoli in magazzino.
#  Hai una lista di tutte le bevande disponibili nel tuo ristorante. Prima della cena,
#  un cliente ha prenotato tutte le bottiglie di un particolare vino per un evento,
#  quindi devi rimuovere quel vino dalla lista delle bevande disponibili. Come lo fai?
# La tua lista di bevande è come segue:
#  bevande = [’acqua’, ’cola’, ’birra’, ’vino bianco’, ’vino rosso’, ’succo di frutta’, ’vino rosso’, ’vino bianco’, ’vino rosso’].
#  Il cliente ha prenotato tutte le bottiglie di ’vino rosso’.
#  Come rimuovi tutte le occorrenze di ’vino rosso’ dalla lista?

bevande = ["acqua", "cola", "birra", "vino bianco", "vino rosso", "succo di frutta", "vino rosso", "vino bianco", "vino rosso"]

while "vino rosso" in bevande:
    bevande.remove("vino rosso")

print(bevande)


