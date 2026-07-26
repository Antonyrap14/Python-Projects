vendite = [
    {"nome_prodotto": "caffé", "importo": 5.00},
    {"nome_prodotto": "torta", "importo": 7.50},
    {"nome_prodotto": "caffé", "importo": 5.00},
    {"nome_prodotto": "gelato", "importo": 3.50},
]

dizionario = {}
for elemento in vendite:
    prodotto = elemento["nome_prodotto"]
    importo = elemento["importo"]
    if prodotto not in dizionario:
        dizionario[prodotto] = importo
    else:
        dizionario[prodotto] += importo
print(dizionario)