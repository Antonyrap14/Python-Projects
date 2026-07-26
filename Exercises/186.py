prezzi_frutta = {
    "mele": 3.50, "banane": 2.00,
    "ciliegie": 8.00, "arance": 4.00
}

def sconto(prezzo:float)->float:
    scontato = prezzo - (prezzo * 0.20) 
    return scontato

new_prezzi = {
    nome:sconto(prezzo)
    for nome,prezzo in prezzi_frutta.items()

}
print(new_prezzi)