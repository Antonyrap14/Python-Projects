prodotti_scorte = [
    ("laptop", 5), ("smartphone", 10),
    ("tablet", 3), ("smartwatch", 7), 
    ("headphones", 15)
]
    

def createDict(lista):
    dictionary = {
       element :prodotti for element,prodotti  in lista
        
    }
    return dictionary

print(createDict(prodotti_scorte))