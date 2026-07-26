libri = int(input("quanti libri hai in prestito?"))

if libri < 5:
    maxvook = 5 - libri
    print(f"puoi prenderli in prestito {maxvook}")
else:
    print("non puoi prenderne in prestito mi spiace|")
