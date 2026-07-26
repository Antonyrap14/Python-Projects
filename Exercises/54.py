libri = {
    "hr":{
        "autore":"rl",
        "anno":2000,
        "prezzo":20
    },
    "sith":{
        "autore":"boh",
        "anno":1945,
        "prezzo":15
    }
}

def modifica_prezzo(dizionario,libro,prezzo):
    if libro in dizionario:
        dizionario[libro]={"prezzo":prezzo}
    else:
        print(f"mi spiace ma il libro {libro} non è presente")

def aggiungi_libro(dizionario,libro,prezzo,autore,anno):
    if libro not in dizionario:
        dizionario[libro]={
            "autore":autore,
            "prezzo":prezzo,
            "anno":anno
        }
def rimuovi(dizionario,libro):
    if libro in dizionario:
        dizionario.pop(libro)
        print("libro rimosso",libro)

def cerca(dizionario,libro):
    if libro in dizionario:
        print(f"trovato il libro {libro}")
    else:
        print("non trovato")

modifica_prezzo(libri,"hr",80)
aggiungi_libro(libri,"ola",2000,"lo",1998)
rimuovi(libri,"hr")
cerca(libri,"ola")
print(libri)
