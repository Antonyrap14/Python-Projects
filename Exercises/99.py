recensioni =  ["Il cibo era fantastico", "Servizio pessimo", "Cibo delizioso", "Ambiente accogliente"]

def cerca(recensioni,parola):
    recensioni_cercate = []
    parola = parola.lower()

    for elemento in recensioni:
        if parola in elemento.lower():
            recensioni_cercate.append(elemento)
    
    return recensioni_cercate

print(cerca(recensioni,parola="cibo"))

def trova_recensioni_con_parola_chiave(
    recensioni, parola_chiave
):
    parola_chiave = parola_chiave.lower()
    recensioni_filtrate = [
        recensione
        for recensione in recensioni
        if parola_chiave in recensione.lower()
    ]
    return recensioni_filtrate

# Esempio di utilizzo
recensioni = [
    "Il cibo era fantastico",
    "Servizio pessimo",
    "Cibo delizioso",
    "Ambiente accogliente",
]
parola_chiave = "cibo"
risultato = trova_recensioni_con_parola_chiave(
    recensioni, parola_chiave
)
print(risultato)  
# Output: ["Il cibo era fantastico", "Cibo delizioso"]


