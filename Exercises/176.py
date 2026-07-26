transaction = [
    {"id":1,"amount":300},
    {"id":2,"amount":5000},
    {"id":3,"amount":100},
    {"id":4,"amount":20},
    {"id":5,"amount":3000},
]

#MIO
def over_1000(transaction):
    new_list = [
        element for element in transaction for id,amount in element.items() if amount >= 1000
    ]

    return new_list

print(over_1000(transaction))

#SUO
# Utilizzo di una list comprehension per filtrare
# le transazioni di alto valore
transazioni_alto_valore = [
    transazione
    for transazione in transaction
    if transazione["amount"] > 1000
]

# Stampa delle transazioni di alto valore
print(transazioni_alto_valore)
print("---------------------------------------------------") 