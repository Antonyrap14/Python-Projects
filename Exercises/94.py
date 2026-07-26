text = """Ciao il sito www.vecchio.it verrà dismesso. \nTutti i libri in merito a www.vecchio.it saranno garantiti"""

def sostituisci(text):
    text = text.replace("www.vecchio.it","www.nuovo.it")
    return text

print(sostituisci(text))