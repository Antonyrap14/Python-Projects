import os

def creaStrutturaCartelle(progetto):
    try:
        os.mkdir(progetto)
        print(f"Creata la cartella principale: {progetto}")
    except FileExistsError:
        print(f"La cartella {progetto} esiste già!")

    # CREAZIONE SOTTOCARTELLE
    sottocartelle = ["Dati", "Risultati", "Documenti"]

    for sottocartella in sottocartelle:
        path = os.path.join(progetto, sottocartella)
        print("Sto creando le cartelle in:", os.getcwd())
        try:
            os.mkdir(path)
            print(f"Creata la cartella {path}")
        except FileExistsError:
            print(f"La cartella {path} esiste già")

# Main
progetto = input("Inserisci nome cartella: ")
creaStrutturaCartelle(progetto)