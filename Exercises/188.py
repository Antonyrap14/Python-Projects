prodotti_prezzi_euro = [("pane", 1.5), ("latte", 0.99), ("uova", 2.2), ("burro", 3.5)] 
tasso_conversione = 1.1

dictionaary = {
    element : round((price * 1.1),2) for element,price in prodotti_prezzi_euro
}
print(dictionaary)