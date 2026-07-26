prezzi_iniziali = {
    "pane": 2.00,
    "latte": 1.50,
    "uova": 3.00,
}


prezzi_finali = {
    element : value * 0.10 + value
    for element,value in prezzi_iniziali.items()
}

print(prezzi_finali)