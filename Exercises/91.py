def censura(testo,volgare):
    for word in volgare:
        elimina = "*" * len(word)
        testo = testo.replace(word,elimina)


    return testo

lista = "no digimon viva"
lista1 = ["no","oi","digimon","pokemon"]

print(censura(lista,lista1))