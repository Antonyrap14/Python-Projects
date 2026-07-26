library = "Pino, Pask, Peppe Pongracic, Sole e mare, Terra e cielo, Mare di mimmo"
parola_chiave = "mare"

def search(library,key_word):
    result = []
    components = library.split(", ")
    key_word = key_word.lower()

    for book in components:
        if key_word in book.lower():
            result.append(book)
    
    for elemenent in result:
        print(elemenent)

search(library,parola_chiave)
