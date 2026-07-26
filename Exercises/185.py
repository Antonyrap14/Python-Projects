nomi = ['Mario Rossi', 'Luca Bianchi', 'Anna Verdi', 'Giulia Neri']

def estraiCognomi(nome):
    name = nome.split(" ")
    cognome = name[1] 
    
    return cognome

new_nomi = [
    estraiCognomi(cognome) for cognome in nomi
]

print(new_nomi)
print(estraiCognomi("Pazza Pizza"))   

