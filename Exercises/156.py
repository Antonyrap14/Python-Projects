magazzino = {}

def add_product(name:str,quantity:int,price:float) -> dict:
    global magazzino
    magazzino[name] = {
        "quantity": quantity,
        "price_per_unit": price,
    }
    return magazzino

def update_quantity(name: str, quantity: int) -> dict:
    global magazzino

    if name in magazzino:
        magazzino[name]["quantity"] = quantity
        return magazzino
    else:
        return "Prodotto inesistente"

def total_value() -> float:
    global magazzino
    total = 0

    for elemento in magazzino:
        prodotto = magazzino[elemento]["price_unit"]* magazzino[elemento]["quantity"]
        total += prodotto
        print(f"{magazzino[elemento]}, prezzo {magazzino[elemento]["price_unit"]}")

    print("Totale")

print(add_product("pasta",12,5.99))
print(add_product("sushi",20,5.99))
total_value()
print(update_quantity("pasta",70))