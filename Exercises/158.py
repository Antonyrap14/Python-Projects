#Immagina di lavorare per un negozio online che vende vari prodotti.
#  Ogni prodotto ha un prezzo base e una tassa fissa applicata.
#  La tua missione è creare una funzione in Python che calcola il prezzo finale di un prodotto.
#  La funzione deve accettare due argomenti di tipo esplicito: prezzo_base di tipo float e tassa_percentuale di tipo float.
#  Il tipo di ritorno della funzione sarà un float che rappresenta il prezzo finale dopo l’applicazione della tassa.
#  Scrivi una funzione denominata calcola_prezzo_finale che riceve il prezzo base e l’imposta come parametri e restituisce il prezzo finale.


def prezzo(prezzo_base:float,tassa:float) -> float:
    prezzo_finale = (prezzo_base * tassa / 100) + prezzo_base
    return prezzo_finale

prodotti = [("pizza",10,3),("pasta",5,3),("pesce",30,10)]
for prodotto,price,tassa in prodotti:
    print(f"{prodotto} ha la tassa {tassa} e il prezzo {price}\nIl prezzo finale è {prezzo(price,tassa)}")
print = "-----------------------------------------------------------------------------------------------"

