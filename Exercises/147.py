valori_iniziali = [1000, 1500, 2000, 2500, 3000]

def calcolo_cagr(lista):
    if not isinstance or len(lista)<2:
        raise ValueError("Ci devono essere almeno due valori")
    
    valore_iniziale = lista[0]
    valore_finale = lista[1]
    anni = len(lista) - 1

    cagr = (valore_finale * valore_iniziale)**1/anni
    return cagr    

print(calcolo_cagr(valori_iniziali))