prezzi = [100.0, 200.0, 300.0, 400.0, 500.0]

def sconti(prezzi):
    new_prezzi =[
        round((prezzo - (prezzo*0.10)),2)
        for prezzo in prezzi
    ]

    return new_prezzi

print(sconti(prezzi))