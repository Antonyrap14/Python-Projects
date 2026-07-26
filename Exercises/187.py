studenti = ["Alice", "Bob", "Charlie", "Diana"]  
punteggi = [85, 92, 78, 90]

def createDict(studenti, punteggi):
    d = {}
    for i in range(len(studenti)):
        d[studenti[i]] = punteggi[i]
    return d

def maggOtt(d):
    new_dict = {} 
    for student,value in d.items():
        if value >= 80:
            new_dict[student] = value
    return new_dict

createDict(studenti, punteggi)
print(maggOtt(createDict(studenti,punteggi)))



dictionario = {
studenti[i]: punteggi[i]
    for i in range(len(studenti))
    if punteggi[i] >= 80
}

print(dictionario)


