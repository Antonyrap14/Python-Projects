prodotti = [
    {
        "nome": "Laptop",
        "quantità": 15,
        "prezzo_unitario": 899.99,
    },
    {
        "nome": "Penna",
        "quantità": 125,
        "prezzo_unitario": 1.25,
    },
    {
        "nome": "Taccuino",
        "quantità": 58,
        "prezzo_unitario": 2.99,
    },
    ]

print(
    "{:<20} {:>10} {:>10}".format(
        "Nome", "Quantità", "Prezzo"
    )
)
print("=" * 40)
for prodotto in prodotti:
    nome = prodotto["nome"]
    quantità = prodotto["quantità"]
    prezzo_unitario = prodotto["prezzo_unitario"]
    print(
        "{:<20} {:>10d} {:>10.2f}".format(
            nome, quantità, prezzo_unitario
        )
    )
