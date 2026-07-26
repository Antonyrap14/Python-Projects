dizionario = {"Laptop": 5,
                "Mouse": 25,
                "Tastiera": 10,
                "Monitor": 7,
            }

def rimuovi(inventario,prodotto):

    if prodotto in inventario:
        del inventario[prodotto]
    
    return inventario

print(rimuovi(dizionario,"Laptop"))
