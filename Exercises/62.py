set = {"Endriu","TonyM","Deimos","Fuze","Kapkan"}

def remove_user(set,nome):
    if nome in set:
        set.discard(nome)
    else:
        print(f"Utente {nome} non prensente")

scegli = ""
while scegli == "si" or scegli == "":
    nome = input("Inserisci un nome:")
    remove_user(set,nome)
    scegli = input("Ne vuoi rimuovere un altro?")
print(set)