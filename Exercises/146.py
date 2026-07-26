def sconto(prezzo,discount=0,promo=0):
    prezzo_sottrarre = (prezzo*discount) / 100
    prezzo_scontato = prezzo - prezzo_sottrarre
    
    if promo and discount:
        prezzo_promo = (prezzo_scontato*5) / 100
        prezzo_finale = prezzo_scontato - prezzo_promo
        return prezzo_finale

    if discount:
        return prezzo_scontato

    
#MAIN
prezzo = float(input("Inserisci prezzo: "))
disconto = float(input("inserisci sconto"))

promozione = input("Hai un codice promozionale?")
if promozione.lower() == "si":
    discount1 = 5
    print(sconto(prezzo,disconto,discount1))
else:
    print("Non hai sconti, il totale è:")
    print(sconto(prezzo,disconto))