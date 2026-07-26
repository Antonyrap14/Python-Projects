articoli = {
    "001":{
        "nome": "Laptop",
        "prezzo": 799.99,
        "quantita": 15
    },
        "002":{
        "nome": "Pc",
        "prezzo": 350.99,
        "quantita": 56
    },
        "003":{
        "nome": "mouse",
        "prezzo": 79.99,
        "quantita": 400
    }
}

def aggiungiarticolo(dizionario,prodotto,nome,quantita,prezzo):
    if prodotto not in dizionario:
        dizionario[prodotto] = {
            "nome" : nome,
            "quantita" : quantita,
            "prezzo":prezzo 
            }
    else:
        print(f"Prodotto già nel dizionario, mi spiace il codice {prodotto} è occupato")
    print(dizionario)
    print(" ")

aggiungiarticolo(articoli,"003","iphone",12,2000)

def aggiornaquantita(dizionario,id,quantita):
    if id in dizionario:
        quantita = int(input("inserisci una quantita"))
        dizionario[id]["quantita"]= quantita
    print(dizionario)
    print("")

aggiornaquantita(articoli,"001",12)

def cerca(dizionario,id):
    if id in dizionario:
        print(f"Il prodotto c'è:\n {dizionario[id]}")
    else:
        print("il prodotto non c'è")

cerca(articoli,"002")

