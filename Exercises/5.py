#Immagina di dover sviluppare un semplice programma in Python per gestire una lista della spesa.
#Il programma deve permettere all’utente di aggiungere elementi alla lista e visualizzare la lista aggiornata.
#Segui i passi sotto per completare l’esercizio: 
# Inizializza una lista vuota chiamata lista_spesa.
# Chiedi all’utente di inserire il nome di un articolo da aggiungere alla lista.
# Aggiungi l’articolo inserito dall’utente alla lista lista_spesa.  
# Mostra all’utente la lista aggiornata.

lista_spesa = []

def aggiungi(lista):
    flag = True
    while(flag):
        scegli = input("Vuoi inserire un elemento alla lista della spesa? s/n: ")
        if scegli == "s":
            elemento = input("inserisci elemento: ")
            lista.append(elemento)
            print(f"{elemento} aggiunto alla lista della spesa")
        else:
            flag = False
    print(lista)

aggiungi(lista_spesa)
    