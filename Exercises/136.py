def cerca_7():
    lista = []

    while(True):
        inserisci = int(input("Inserisci un numero,se metti il 7 termina subito!: "))
        lista.append(inserisci)
        if inserisci == 7:
            print("hai inserito il 7 nella lista:\n{0}".format(lista))
            break
#MAIN
cerca_7()
        

