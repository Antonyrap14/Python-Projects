def calcola_prezzo_totale(
    carrello: list[tuple[str, float]]
) -> float:
    tot = 0
    for nome,prezzo in carrello:
        print(f"{nome}:{prezzo}")
        tot += prezzo
    return tot

carrello = [("mela", 0.5), ("pane", 1.2), ("latte", 1.5)]
print(calcola_prezzo_totale(carrello))


