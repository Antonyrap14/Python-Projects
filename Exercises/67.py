promozione = ["pizza","pane","pasta"]
prodotti = ["pizza","sushi","kebab","pasta"]

promozione = set(promozione)
prodotti = set(prodotti)

intersezione =  prodotti - promozione

print(intersezione)

intersect = prodotti.intersection(promozione)
print(intersect)