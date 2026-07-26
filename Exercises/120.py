livello_acqua = int(input("Scrivi quanti cm di acqua ci sono: "))

def critical(acqua):
    if acqua <= 20:
        print("Situazione normale")
    elif  20 < acqua <= 50:
        print("Allerta")
    elif  50 < acqua <= 100:
        print("Emergenza")
    else:
        print("evaquare")

critical(livello_acqua)
