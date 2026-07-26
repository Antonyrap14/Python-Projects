def controllo_accesso(eta,livello_accesso):
    accesso = livello_accesso.lower()

    if eta < 18:
        print("accesso negato!")

    else:
        if accesso == "admin":
            print("accesso come admin")
        elif accesso == "user":
            print("accesso come user")
        elif accesso == "guess":
            print("guess")
        else:
            print("Intruso!!!")

eta = int(input("scrivi eta "))
livello = input("scrivi il livello ")
controllo_accesso(eta,livello)
    
