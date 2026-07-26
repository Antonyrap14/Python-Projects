euro = [10,22,34,100,20.99,12.23]
conversione_dollaro = 0.85

def convertiEuro(lista,tasso):
    new_list = [
        round((element * 0.85), 2) 
        for element in lista
    ]

    return new_list

print(convertiEuro(euro,conversione_dollaro))