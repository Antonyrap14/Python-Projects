
def fattura(nome,ordine,prodotti_lista):
   receipt = f"La fattura di {nome}\n"
   receipt += f"Fattura numero {ordine}\n Prodotti:\n"
   for elementi in prodotti_lista:
      receipt += f" - {elementi}\n"
    
   print(receipt)

   


lista = ["pasta","pane","succo"]
fattura("Paolo",123,lista)




