def recensioni(lista):
    for product,review in lista:
        print(f"{product}-{review}")

review = [
    ("pizza","Ottima e saporita"),
    ("pasta","Gradevole"),
    ("sfornato","Non ottima la qualità del formaggio"),
    ("tagliere","Ottimi i salumi")
]

recensioni(review)