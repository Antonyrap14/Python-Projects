def generaBiglietto():
    print("---------------------------------")
    nome = input("inserisci nome")
    cognome = input("inserisci cognome")
    titolo = input("inserisci titolo")
    numero = int(input("inserisci numero di telefono"))
    dizionario = {
        "nome":nome,
        "cognome":cognome,
        "numero":numero,
        "titolo":titolo
    }

    for key,value in dizionario.items():
        print(f"{key}:{value}")

    print("-------------------------")

generaBiglietto()
              