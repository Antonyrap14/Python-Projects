libri = {
   1762763782:"il signore degli anelli",
   2832893723:"harry potter",
   2781738947:"calcio"
}
def aggiungi_aggiorna(isbn,titolo,libro):
    variabile = libro[isbn] = titolo
    if variabile in  libro:
        print(f"Il valore aggiornato è:{variabile}")
    else:
        print(f"Il nuovo valore è:{variabile}")

flag = True
while(flag):
    scegli = input("inserisci un valore tra si e no:")
    if scegli == "si":
        titolo = input("inserisci un titolo:")
        isbn = int(input("inserisci il isbn:"))
        aggiungi_aggiorna(isbn,titolo,libri)
    else:
        print(f"il tuo elenco è:{libri}")
        flag = False

