def occorrenza(frase):
    dizionario = {}
    count = 0
    frase = frase.split(" ")

    for parola in frase:
        parola.lower()

        if parola not in dizionario:
            count = 1
            dizionario[parola] = count
        else:
            dizionario[parola] += count
    
    return dizionario

print(occorrenza("Python is great. Python programming is fun. Fun with Python!"))


