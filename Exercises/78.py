def effettua_ordine():
    nome = input("inserisci il tuo nome:")
    prodotto = input("inserisci il prodotto:")
    numero = int(input("inserici il numero del prodotto:"))
    print(f"Caro {nome},\nLa ringraziamo per il suo ordine {numero}. Il prodotto {prodotto} è stato confermato e sarà spedito a breve.\nSaluti dal team")


def mail(nome,numero,prodotto):
    print(f"Caro {nome},\nLa ringraziamo per il suo ordine {numero}. Il prodotto {prodotto} è stato confermato e sarà spedito a breve.\nSaluti dal team")

while True:
    scegli = input("Vuoi fare un ordine? ")
    if scegli == "si":
        effettua_ordine()
    else:
        print("Non vuoi fare alcun ordine")