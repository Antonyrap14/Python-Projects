dipendenti = ["antonio","mattia","mirco","lorenzo","sara","andrea","alessandro","marco"]

def cerca(nome):

    if nome in dipendenti:
        print(f"il dipendeente {nome} è presente. \n {dipendenti}")
    else:
        print("Il nome non c'è")

bool = True
while bool:
    nome = input("inserisci un nome:")
    cerca(nome)
    scegli = input("vuoi ontinuare?")
    if scegli == "n":
        bool = False
    