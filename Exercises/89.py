descrizioni_prodotti = [
    "Prodotto 1: Smartphone con 128 GB di memoria",
    "Prodotto 2: Laptop con 16 GB di RAM e 512 GB SSD",
    "Prodotto 3: Tablet con display da 10 pollici",
]

def parse(descrizione):
    return "\n".join(descrizione)

print(parse(descrizioni_prodotti))