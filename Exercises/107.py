def prezzi(nome,eta):
    if eta >= 12:
        return "{0} paga 30 euro perchè ha {1} anni".format(nome,eta)
    elif eta<12 and eta>3:
        return "{0} paga 15 euro perchè ha {1} anni".format(nome,eta)
    else:
        return "{0} Non paga perchè ha {1} anni".format(nome,eta)

nome = input("Scrivi un nome:")
eta = int(input("scrivi l'età:"))
print(prezzi(nome,eta))
