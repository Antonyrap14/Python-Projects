def maggiorenne(nome,eta):
    if eta > 18:
        print("Assunto poichè sei maggiorenne")
    else:
        print("Mi spiace sei minorenne")

nome = input("Nome")
eta = int(input("eta"))
maggiorenne(nome,eta)
