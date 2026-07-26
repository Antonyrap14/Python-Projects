import random

def indovina_numero():
    flag = True
    numero_random = random.randint(1,10)

    while(flag):
        numero = int(input("inserisci un numero: "))

        if numero_random == numero:
            print(f"Complimenti hai indovinato!\nIl numero era {numero}")
            flag = False
#MAIN
indovina_numero()