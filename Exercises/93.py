def segnaposto(dizionario):
    for key,value in dizionario.items():
        if key == "nome":
            nome = value
        elif key == "prodotto":
            prodotto = value
        elif key == "azienda":
            azienda = value
    print(f"""Ciao {nome},\n
Grazie per il tuo acquisto di {prodotto}!\n 
Ci auguriamo che ti piaccia il tuo nuovo {prodotto}.""")





dictionary = {
    "nome": "Mario Rossi",
    "prodotto": "Notebook XYZ",
    "azienda": "TechSolutions"
}

segnaposto(dictionary)