#In quest’esercizio,
#  lavorerai con una lista di numeri interi in Python.
#  La tua lista inizierà con i numeri da 0 a 9 (inclusi).
#  Il tuo compito è sviluppare un programma che rimuova il terzo, 
# il quinto e l’ottavo elemento dalla lista. Ricorda, gli indici in Python iniziano da 0. 
# Dovresti stampare la lista sia prima che dopo la rimozione degli elementi.

numeri = list(range(10))

del numeri[7]
del numeri[4]
del numeri[2]

print(numeri)