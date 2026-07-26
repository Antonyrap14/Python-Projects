def applica_sconto(prezzo,sconto=10):
    prezzo_scontato = prezzo - ((prezzo * sconto)/100)
    return prezzo_scontato

#MAIN   
prezzo = int(input("Inserisci prezzo: "))
sconto = input("inserisci sconto se no premi invio")

if sconto:
    sconto_intero = int(sconto)
    print(f"Il prezzo scontato {applica_sconto(prezzo,sconto_intero)}")
else:
    print(f"Il prezzo scontato {applica_sconto(prezzo)}")

