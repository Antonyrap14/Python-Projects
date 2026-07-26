prezzi = [
    (100, "USD"),
    (200, "EUR"),
    (150, "GBP"),
]

def converti(lista):
    usd = 0.85   # 1 USD = 0.85 EUR
    gbp = 1.15   # 1 GBP = 1.15 EUR
    
    new_list = [
        element[0] * usd if element[1] == "USD"
        else element[0] * gbp if element[1] == "GBP"
        else element[0]  # EUR rimane uguale
        for element in lista
    ]
    
    return new_list

print(converti(prezzi))
print("------------------------------------------------------------------------------------------")
# Lista di prezzi con valute
prezzi = [
    (100, "USD"),
    (200, "EUR"),
    (150, "GBP"),
    (50, "USD"),
    (300, "GBP"),
]

# Tassi di cambio da altra valuta a Euro
tassi_di_cambio = {
    "USD": 0.85,
    "EUR": 1,
    "GBP": 1.15,
}

# Utilizzando una list comprehension per
# convertire i prezzi in Euro
prezzi_in_euro = [
    prezzo * tassi_di_cambio[valuta]
    for prezzo, valuta in prezzi
]

print(prezzi_in_euro)

