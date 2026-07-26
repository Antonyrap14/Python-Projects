def macchinetta():
    scegli = int(input("Inserisci bevanda:\n1 caffe 1€\n2 acqua 2€\n3 tè 3€"))
    if scegli == 1:
        importo = 1
        bevanda = "Caffe"
    elif scegli == 2:
        importo = 2
        bevanda = "Acqua"
    else:
        importo = 3
        bevanda = "Tè"

    somma = 0
    
    while(True):
        moneta = float(input("inserisci moneta: "))
        somma += moneta
        if somma > importo:
            print(f"il tuo resto è: {somma - importo}")
            break
        elif somma == importo:
            print(f"Tieni la bevanda! {bevanda}")
            break
        else:
            print(f"Ti mancano {importo - somma}€")

macchinetta()