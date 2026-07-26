dipendenti = {
    "Mario":{
        "Progetto A":10,
        "Progetto B":5
    },
      "Massimo":{
        "Progetto A":1,
        "Progetto C":12,
        "Progetto D":8
    },
      "Carlo":{
        "Progetto D":10,
        "Progetto B":50
    },
}

def ore(nome):
    if nome not in dipendenti:
        return "Il dipendente non c'è!"
    
    somma = 0
    if nome in dipendenti:
        for a,dettagli in dipendenti.items():
            for progetto,ore in dettagli.items():
                if a == nome:
                   somma = somma + ore
    return somma


            
nome = input("inserisci il nome del dipendente  ")
nuovo_nome = nome.capitalize()
print(f"Le ore lavorate sono: {ore(nuovo_nome)}")